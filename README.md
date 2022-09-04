# mnist-notebooks

## Install zsh and oh-my-zshell
```bash
apt-get -y install zsh
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

## Create the SSH key for GitHub
```bash
ssh-keygen -t ed25519 -C "farleyknight@gmail.com" 
```

## Cat it to the terminal
```bash
cat ~/.ssh/id_ed25519.pub 
ssh-ed25519 .... farleyknight@gmail.com
```

## Paste that into the SSH keys for GitHub

[Create a new SSH key](https://github.com/settings/ssh/new)

## Set up my email & name
```bash
git config --global user.email "farleyknight@gmail.com"
git config --global user.name "Farley Knight"
```

## Install the proper Python libraries
```bash
pip install wandb seqeval datasets evaluate
```


## Install Git LFS (for HuggingFace)
```bash
apt-get -y install git-lfs
git lfs install
```

## Clone the Transformers Library
```bash
cd /workspace # This is the main directory for vast.ai setups
git clone git@github.com:huggingface/transformers.git
```

## Set up dataset and task name to make model name

```bash
dataset_name='mnist' # https://huggingface.co/datasets/mnist
task_name='digit-classification'
model_name=${dataset_name}-${task_name}
```

## Set up the output directory

```bash
right_now=$(date +'%Y-%m-%d')
output_dir=/workspace/models/${model_name}/${right_now}
```

## Set up the huggingface model id and wandba_project

```bash
model_id=${model_name}-${right_now}
wandb_project=${model_id}
```

## Set up the transformer scripts
```
transformer_scripts='/workspace/transformers/examples/pytorch'
run_img_cls_path=${transformer_scripts}/image-classification/run_image_classification.py
```

## Set up the seed

```bash
seed=42
```

## Start training!

```bash
python $run_img_cls_path \
    --dataset_name mnist \
    --output_dir $output_dir \
    --overwrite_output_dir \
    --remove_unused_columns False \
    --do_train \
    --do_eval \
    --push_to_hub \
    --hub_model_id $model_id \
    --hub_strategy all_checkpoints \
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
```

