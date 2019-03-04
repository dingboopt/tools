#!/bin/bash
sudo apt-get -y install build-essential fakeroot dpkg-dev
mkdir ~/git-rectify
cd ~/git-rectify
sudo apt-get  -y source git
sudo apt-get -y build-dep git
sudo apt-get -y install libcurl4-openssl-dev
sed -i 's/libcurl4-gnutls-dev/libcurl4-openssl-dev/g' git-2.19.1/debian/control 
sed -i '/TEST =test/d' git-2.19.1/debian/rules
cd git-2.19.1
sudo dpkg-buildpackage -rfakeroot -b
cd ..
sudo dpkg -i git_2.19.1-1ubuntu1.1_amd64.deb
