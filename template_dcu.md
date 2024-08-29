# SE-ResNet模型说明文档(DCU)

## 1. 模型概述
SE-ResNet模型，全称为Squeeze-and-Excitation ResNet，是一种集成了Squeeze-and-Excitation（SE）模块的深度残差网络。该模型由牛津大学Visual Geometry Group提出，是对原有ResNet模型的改进。SE模块通过显式地建模通道
间的相互关系，提高了网络的表示能力，特别适用于图像分类和定位任务。

## 2. 原理介绍
SE-ResNet模型在传统的ResNet基础上引入了SE模块，具体结构如下：

1. **SE模块**：通过全局平均池化（Global Average Pooling, GAP）和全连接层捕捉通道间的相互关系，并通过可学习的权重对通道进行重标定，增强了网络的特征提取能力。

2. **卷积层**：使用3x3的卷积核，步幅为1，填充为1，保持了输入和输出的空间维度一致性。每个卷积层后接ReLU激活函数。

3. **残差连接**：SE-ResNet保留了ResNet的残差连接设计，有助于解决深层网络训练中的梯度消失问题。

4. **池化层**：在特征图尺寸较大时使用2x2的最大池化层进行下采样。

5. **全连接层**：模型最后包含几个全连接层，最终输出层为1000维的Softmax层，用于1000类分类任务。

## 3. 数据介绍
ImageNet-1K数据集是计算机视觉领域广泛使用的大型图像数据集，包含1000个类别，每个类别有大约1000张图像。数据集分为训练集、验证集和测试集，具体如下：

- **训练集**：1,281,167张图像，用于模型训练。
- **验证集**：50,000张图像，用于模型调参和效果评估。
- **测试集**：100,000张图像，用于最终模型性能测试。

## 4. 效果评估
SE-ResNet模型在ImageNet-1K数据集上进行了训练和测试，展现出优异的分类性能。模型精度、损失函数值等详细性能指标如下：


V100精度

DCU-K100精度

精度相对误差
（给出误差的具体数值+是否达标结论）

V100效率

DCU-K100效率

|环境配置|V100精度|DCU-K100精度 |精度相对误差|V100效率|DCU-K100效率|效率比例|
|--|--|--|--|--|--|--|--|
|2机16卡|acc=1.0|acc=1.0|达标|throughput:  5788|throughput:  7016|121%|


## 5. 运行环境
- **卡型**：DCU-K100
- **运行卡数**：16卡

## 6. 运行说明
### docker镜像
- 代码及数据及镜像在四个分割的压缩包里：codeAndDataaa  codeAndDataab  codeAndDataac  codeAndDataad

### 运行docker容器

- 加载运行环境

bash
#以防多机之间通讯出现问题，条件允许的话可以先关闭宿主机的防火墙
systemctl stop firewalld

#加载镜像
docker load -i guochanhua-dcu-multi_240417.tar.gz
docker load -i guochanhua-dcu-torch2.1-renet_240326.tar.gz

#创建并进入容器
docker run -it --name dcu-multi-renet  --network=host --ipc=host --privileged --shm-size=128G  -v /data/guochanhua/db/:/guochanhua  --workdir=/guochanhua -v /opt/hyhal:/opt/hyhal --device=/dev/kfd --device=/dev/dri --group-add video --cap-add=SYS_PTRACE --security-opt seccomp=unconfined artifact.cloudwalk.work/rd_docker_release/cw-ai2/guochanhua-dcu-torch2.1-renet:240326 bash
docker run -it --name dcu-multi  --network=host --ipc=host --privileged --shm-size=128G  -v /data/guochanhua/db/:/guochanhua  --workdir=/guochanhua -v /opt/hyhal:/opt/hyhal --device=/dev/kfd --device=/dev/dri --group-add video --cap-add=SYS_PTRACE --security-opt seccomp=unconfined artifact.cloudwalk.work/rd_docker_release/cw-ai2/guochanhua-dcu-multi:240417 bash


### 运行代码
解压后的目录下包含如下20个DCU所有代码和数据集:
SE-ResNet
EfficientNet
ViT
CRNN
Focus_RepVGG
Focus_EfficientNet
DBNet
Swin-Transformer
MGFace
MGN
C3D
TSN
R(2+1)D
TRN
S3D
AV-SlowFast
ST-GCN
GGCN
2S-AGCN
AS-GCN

st-gcn、mgface、as-gcn使用artifact.cloudwalk.work/rd_docker_release/cw-ai2/guochanhua-dcu-torch2.1-renet:240326镜像，其他使用artifact.cloudwalk.work/rd_docker_release/cw-ai2/guochanhua-dcu-multi:240417镜像


### 运行代码
首先合并并解压压缩包：
bash
cat codeAndDataa* >codeAndData.tar.gz && tar xvzf codeAndData.tar.gz

以SE-ResNet为例：

#### 运行SE-ResNet模型
- 启动对应container
- 进入Training/exe-cmd/SEResNet/目录，
- 双机脚本 main-SEResNet.sh、	slave-SEResNet.sh
- 修改运行脚本的参数，主服务器修改main-SEResNet.sh文件，从服务器修改slave-SEResNet.sh文件
- 修改--master\_addr为主服务器ip地址
- 默认参数是2机16卡运行，如果是其他类型，可以按需修改--nproc\_per\_node、--nnodes、--num\_workers等参数
- 比如说单机16卡运行，修改--nproc\_per\_node 16、--nnodes 1、--num\_workers 16

bash
docker run -it --name dcu-multi  --network=host --ipc=host --privileged --shm-size=128G  -v /data/guochanhua/db/:/guochanhua  --workdir=/guochanhua -v /opt/hyhal:/opt/hyhal --device=/dev/kfd --device=/dev/dri --group-add video --cap-add=SYS_PTRACE --security-opt seccomp=unconfined artifact.cloudwalk.work/rd_docker_release/cw-ai2/guochanhua-dcu-multi:240417 bash
cd Training/exe-cmd/SEResNet/

#修改运行脚本的master_addr参数，主服务器修改train.sh文件，从服务器修改trainn.sh文件
#主副服务器的区别在于--node_rank参数，主服务器为0，从服务器为1
vi main-SEResNet.sh
vi slave-SEResNet.sh

#运行代码，主服务器运行train.sh文件，从服务器运行trainn.sh文件
bash main-SEResNet.sh nolog
bash slave-SEResNet.sh nolog
'''
