#!/bin/bash

## Add Python/Pip to environment
eval "$(/root/anaconda3/bin/conda shell.bash hook)"

## Install the proper Python libraries
pip install wandb seqeval datasets evaluate torch torchvision
pip install git+https://github.com/huggingface/transformers

# Login to HuggingFace
pip install huggingface_hub
python -c "from huggingface_hub.hf_api import HfFolder; HfFolder.save_token('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')"

## Install Git LFS (for HuggingFace)
apt-get -y install git-lfs
git lfs install

## Clone the Transformers Library
cd /workspace # This is the main directory for vast.ai setups
git clone git@github.com:huggingface/transformers.git
