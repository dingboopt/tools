from openai import OpenAI
from pathlib import Path
import sys
import pandas as pd

# Replace 'file_path.xlsx' with the path to your Excel file
file_path = sys.argv[1]

# Load the Excel file
df = pd.read_excel(file_path)

# Display the first few rows of the dataframe
print(df.head())


file_path = Path(sys.argv[2])

# 使用read_text()方法直接读取文件内容到字符串
template_mlu = file_path.read_text(encoding='utf-8')

file_path = Path(sys.argv[3])

# 使用read_text()方法直接读取文件内容到字符串
template_dcu = file_path.read_text(encoding='utf-8')

for index, row in df.iloc[:].iterrows():  # Start iterating from the second row
    # Access a specific field by column name
    #field_value = row['column_name']  # Replace 'column_name' with your actual column name
    #model a\环境配置b\V100精度c\MLU370精度d\精度相对误差e\V100效率f\MLU370效率g\效率比例h\数据集j\hardware k
    # Alternatively, access a specific field by column index
    field_value = row[0]  # 0 corresponds to the first column
    a,b,c,d,e,f,g,h,j,k = tuple(row)
    #promt = f'\n参照如下文档，写一篇{a}在{j}数据集上的文档,尽可能详细，文档标题中{k}的部分保持不变，运行环境部分保持不变，效果评估数据|环境配置|V100精度|MLU370精度 |精度相对误差|V100效率|MLU370效率|效率比例|\n|--|--|--|--|--|--|--|--|\n {b}|{c}|{d}|{e}|{f}|{g}|{h}：\n\n\\n\n'
    print(f'{a}-{k}: |{b}|{c}|{d}|{e}|{f}|{g}|{h:.2%}|')
    promt = f'\n参照如下文档，写一篇{a}在{j}数据集上的文档,尽可能详细，文档标题中{k}的部分保持不变，运行环境部分保持不变，效果评估数据{b}\t{c}\t{d}\t{e}\t{f}\t{g}\t{h}：\n\n\\n\n'
    if k=='MLU':
        file_content = template_mlu
    else:
        file_content = template_dcu
    content = f'{promt}{file_content}'
    #continue
    #print(content)

    client = OpenAI()
    completion = client.chat.completions.create(
      model="gpt-4o-mini",
      messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": content}
      ]
    )
    
    print(f'############\n')
    print(completion.choices[0].message.content)
    #raise
    file_path = f'./{a}-{k}.md'
    with open(file_path, 'w') as file:
        file.write(completion.choices[0].message.content)


    
raise

client = OpenAI()

file_path = Path(sys.argv[1])

# 使用read_text()方法直接读取文件内容到字符串
file_content = file_path.read_text(encoding='utf-8')

raise
promt = f'\n参照如下文档，写一篇{a}在{j}数据集上的文档,尽可能详细，文档标题中{k}的部分保持不变，运行环境部分保持不变，效果评估数据{b}\t{c}\t{d}\t{e}\t{f}\t{h}：\n\n\\n\n{file_content}'
#s =f'\n参照如下文档，写一篇EfficientNet在ucf101数据集上的文档,尽可能详细，文档标题中DCU的部分保持不变，运行环境部分保持不变，效果评估数据2机16卡\tacc=0.9\tacc=1.0\t达标\tthroughput:  5788\tthroughput:  7016\t121%：\n\n\\n\n{file_content}'
#s= '\n参照如下文档，写一篇EfficientNet在coco数据集上的文档，文档标题中MLU的部分保持不变，运行环境部分保持不变， 效果评估数据2机16卡\tacc=0.9\tacc=1.0\t达标\tthroughput:  5788\tthroughput:  7016\t121%：\n\n\n# SE-ResNet模型说明文档(MLU)\n\n## 1. 模型概述\nSE-ResNet模型，全称为Squeeze-and-Excitation ResNet，是一种集成了Squeeze-and-Excitation（SE）模块的深度残差网络。该模型由牛津大学Visual Geometry Group提出，是对原有ResNet模型的改进。SE模块通过显式地建模通道间的相互关系，提高了网络的表示能力，特别适用于图像分类和定位任务。\n\n## 2. 原理介绍\nSE-ResNet模型在传统的ResNet基础上引入了SE模块，具体结构如下：\n\n1. **SE模块**：通过全局平均池化（Global Average Pooling, GAP）和全连接层捕捉通道间的相互关系，并通过可学习的权重对通道进行重标定，增强了网络的特征提取能力。\n\n2. **卷积层**：使用3x3的卷积核，步幅为1，填充为1，保持了输入和输出的空间维度一致性。每个卷积层后接ReLU激活函数。\n\n3. **残差连接**：SE-ResNet保留了ResNet的残差连接设计，有助于解决深层网络训练中的梯度消失问题。\n\n4. **池化层**：在特征图尺寸较大时使用2x2的最大池化层进行下采样。\n\n5. **全连接层**：模型最后包含几个全连接层，最终输出层为1000维的Softmax层，用于1000类分类任务。\n\n## 3. 数据介绍\nImageNet-1K数据集是计算机视觉领域广泛使用的大型图像数据集，包含1000个类别，每个类别有大约1000张图像。数据集分为训练集、验证集和测试集，具体如下：\n\n- **训练集**：1,281,167张图像，用于模型训练。\n- **验证集**：50,000张图像，用于模型调参和效果评估。\n- **测试集**：100,000张图像，用于最终模型性能测试。\n\n## 4. 效果评估\nSE-ResNet模型在ImageNet-1K数据集上进行了训练和测试，展现出优异的分类性能。模型精度、损失函数值等详细性能指标如下：\n\n\nV100精度\n\nMLU370精度\n\n精度相对误差\n（给出误差的具体数值+是否达标结论）\n\nV100效率\n\nMLU370效率\n\n|环境配置|V100精度|MLU370精度 |精度相对误差|V100效率|MLU370效率|效率比例|\n|--|--|--|--|--|--|--|--|\n|2机16卡|acc=1.0|acc=1.0|达标|throughput:  5788|throughput:  7016|121%|\n\n\n## 5. 运行环境\n- **卡型**：MLU370\n- **运行卡数**：16卡\n\n## 6. 运行说明\n### docker镜像\n\n- 镜像压缩包：guochanhua-dcu-multi_240117.tar.gz 该镜像中包括DCU运行环境\n- 代码及数据：code_data.tar.gz\n\n### 运行docker容器\n\n- 加载运行环境\nbash\n#以防多机之间通讯出现问题，条件允许的话可以先关闭宿主机的防火墙\nsystemctl stop firewalld\n\n#加载镜像\ndocker load -i guochanhua-mlu-v1.18.0-torch1.13.1_20240409.tar.gz\n\n#创建并进入容器\ndocker run -it --name=mlu-multi-v1.18-240129  --network=host --ipc=host --privileged  --shm-size 100G -w /code  -v /usr/bin/cnmon:/usr/bin/cnmon  -v /data/guochanhua/xxx/db/:/guochanhua -w /guochanhua  artifact.cloudwalk.work/rd_docker_release/cw-ai2/guochanhua-mlu-v1.18.0-torch1.13.1:20240409\n\n### 运行代码\n解压后的目录下包含如下10个MLU所有代码和数据集:\nMG-ShuffleNetV1\nMG-ShuffleNetV2\nResNet+FPN\nMTCNN\nEfficientNet+FPN\nCRNN\nSE-ResNet\nEfficientNet\nViT\nC3D\n\n#### 运行SE-ResNet模型\n\n- 进入Training/exe-cmd/seresNet-timm/目录，\n- 双机脚本 main-seresnet.sh、\tslave-seresnet..sh\n- 修改运行脚本的参数，主服务器修改main-seresnet.sh文件，从服务器修改slave-seresnet.sh文件\n- 修改--master\\_addr为主服务器ip地址\n- 默认参数是2机16卡运行，如果是其他类型，可以按需修改--nproc\\_per\\_node、--nnodes、--num\\_workers等参数\n- 比如说单机16卡运行，修改--nproc\\_per\\_node 16、--nnodes 1、--num\\_workers 16\nbash\ncd Training/exe-cmd/seresNet-timm/\n\n#修改运行脚本的master_addr参数，主服务器修改train.sh文件，从服务器修改trainn.sh文件\n#主副服务器的区别在于--node_rank参数，主服务器为0，从服务器为1\nvi main-seresnet.sh\nvi slave-seresnet.sh\n\n#运行代码，主服务器运行train.sh文件，从服务器运行trainn.sh文件\nbash main-seresnet.sh nolog\nbash slave-seresnet.sh nolog\n### 注意事项\n- NA\n'
print(prompt)
raise
completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": s}
  ]
)

print(completion.choices[0].message)
print(f'############\n')
print(completion.choices[0].message.content)
