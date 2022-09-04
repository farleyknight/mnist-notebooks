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

# Login to HuggingFace
pip install huggingface_hub
python -c "from huggingface_hub.hf_api import HfFolder; HfFolder.save_token('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')"

## Install Git LFS (for HuggingFace)
apt-get -y install git-lfs
git lfs install

## Clone the Transformers Library
cd /workspace # This is the main directory for vast.ai setups
git clone git@github.com:huggingface/transformers.git

## Set up dataset and task name to make model name
dataset_name='mnist' # https://huggingface.co/datasets/mnist
task_name='digit-classification'
model_name=${dataset_name}-${task_name}

## Set up the output directory
right_now=$(date +'%Y-%m-%d')
output_dir=/workspace/models/${model_name}/${right_now}

## Set up the huggingface model id and wandba_project
model_id=${model_name}-${right_now}
wandb_project=${model_id}

## Set up the transformer scripts
transformer_scripts='/workspace/transformers/examples/pytorch'
run_img_cls_path=${transformer_scripts}/image-classification/run_image_classification.py

## Set up the seed
seed=42

## Start training!
python $run_img_cls_path \
    --dataset_name mnist \
    --output_dir $output_dir \
    --overwrite_output_dir \
    --remove_unused_columns False \
    --do_train \
    --do_eval \
    --push_to_hub \
    --hub_model_id $model_id \
    --hub_strategy every_save \
    --learning_rate 2e-5 \
    --num_train_epochs 5 \
    --per_device_train_batch_size 8 \
    --per_device_eval_batch_size 8 \
    --logging_strategy steps \
    --save_steps 100 \
    --logging_steps 100 \
    --eval_steps 1000 \
    --save_strategy steps \
    --save_total_limit 3 \
    --seed $seed
