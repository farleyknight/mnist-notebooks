#!/bin/bash

export PATH=/opt/conda/bin:$PATH
eval "$(conda shell.bash hook)"

# Install GCC compiler, to compile C extensions
apt-get -y install gcc g++
# Install BLAS/PACK for linear algebra libraries for ML
apt-get -y libblas3 liblapack3 liblapack-dev libblas-dev
# Install a text editor & Git LFS (for HuggingFace)
apt-get -y install vim git-lfs

## Install the proper Python libraries
pip install wandb huggingface_hub seqeval datasets evaluate torch rouge_score
pip install git+https://github.com/huggingface/transformers

# Login to HuggingFace and W&B
python -c "from huggingface_hub.hf_api import HfFolder; HfFolder.save_token('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')"
wandb login 760d6f682b2978cc4db05e6ec7e5ced94972a47c

## Install zsh and oh-my-zshell
apt-get -y install zsh && sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
