#!/bin/bash

echo -e "Setting up an Ubuntu Workstation" && sleep 5

packages="golang rustc openjdk-11-jdk"
packages="$packages maven"
packages="$packages python3 python3-pip python3-venv"
packages="$packages vim git tree"

sudo apt update
sudo apt upgrade

sudo apt install -y ${packages}
