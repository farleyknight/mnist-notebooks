#!/bin/bash

## Set up my email & name. Also create the SSH key.
git config --global user.email "farleyknight@gmail.com"
git config --global user.name "Farley Knight"
ssh-keygen -t ed25519 -C "farleyknight@gmail.com"

## Clone the Transformers Library
mkdir -p /workspace # This is the main directory for vast.ai setups
cd /workspace
git clone git@github.com:huggingface/transformers.git

## Set up the project
git clone git@github.com:farleyknight/mnist-notebooks.git
