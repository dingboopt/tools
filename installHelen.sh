#!/bin/bash
git clone https://github.com/HelenOS/helenos.git

if [ -f /etc/apt/apt.conf ]; then
   echo "apt.conf exists"
else
   echo "create apt.conf"
   touch /etc/apt/apt.conf
fi
echo 'Acquire::http::Proxy "false";' > /etc/apt/apt.conf

apt update
sudo apt-get install python build-essential libgmp-dev libmpfr-dev ppl-dev libmpc-dev zlib1g-dev texinfo libtinfo-dev xutils-dev bison flex
cd HelenOS/tools
./toolchain.sh amd64
cd ..
make PROFILE=amd64
./tools/ew.py -nokvm
