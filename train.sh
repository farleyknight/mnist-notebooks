#!/usr/bin/zsh

# Set up the machine for ML training

## Install zsh and oh-my-zshell
apt-get -y install zsh
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

## Set up my email & name
git config --global user.email "farleyknight@gmail.com"
git config --global user.name "Farley Knight"

## Install the proper Python libraries
pip install wandb seqeval datasets evaluate
pip install git+https://github.com/huggingface/transformers

