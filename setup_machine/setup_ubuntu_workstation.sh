#!/bin/bash

echo -e "Setting up an Ubuntu Workstation" && sleep 5

packages="golang"
packages="$packages rustc"
packages="$packages vim"
packages="$packages git"
packages="$packages python3"
packages="$packages tree"

sudo apt update
sudo apt upgrade

sudo apt install -y ${packages}
