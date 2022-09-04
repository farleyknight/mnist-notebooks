#!/bin/bash

## Set up my email & name
git config --global user.email "farleyknight@gmail.com"
git config --global user.name "Farley Knight"

## Set up Python & Conda
cd /workspace
wget https://repo.anaconda.com/archive/Anaconda3-2022.05-Linux-x86_64.sh
chmod +x Anaconda3-2022.05-Linux-x86_64.sh
./Anaconda3-2022.05-Linux-x86_64.sh
eval "$(/root/anaconda3/bin/conda shell.bash hook)"
conda init

## Install zsh and oh-my-zshell
apt-get -y install zsh
rm -rf /root/.oh-my-zsh
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

## Create new SSH key
ssh-keygen -t ed25519 -C "farleyknight@gmail.com" 