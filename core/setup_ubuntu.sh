#!/bin/bash

# set up env for Linux ubuntu
sudo apt-get install openjdk-8-jdk
sudo apt-get install maven
sudo apt-get install build-essential autoconf automake libtool cmake zlib1g-dev pkg-config libssl-dev


# install protobuf 2.5
curdir=$PWD
cd /usr/local/src/
sudo wget https://github.com/google/protobuf/releases/download/v2.5.0/protobuf-2.5.0.tar.gz
sudo tar xvf protobuf-2.5.0.tar.gz
cd protobuf-2.5.0
sudo ./autogen.sh
sudo ./configure --prefix=/usr
sudo make
sudo make install
protoc --version

cd $curdir
