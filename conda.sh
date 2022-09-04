#!/usr/bin/zsh

cd /workspace
wget https://repo.anaconda.com/archive/Anaconda3-2022.05-Linux-x86_64.sh

chmod +x Anaconda3-2022.05-Linux-x86_64.sh
./Anaconda3-2022.05-Linux-x86_64.sh

eval "$(/root/anaconda3/bin/conda shell.zsh hook)"

conda init