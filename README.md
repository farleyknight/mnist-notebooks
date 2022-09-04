# mnist-notebooks

## Create the SSH key for GitHub
```
ssh-keygen -t ed25519 -C "farleyknight@gmail.com" 
```

## Set up my email & name
```
git config --global user.email "farleyknight@gmail.com"
git config --global user.name "Farley Knight"
```

## Install the proper Python libraries
```
pip install wandb seqeval datasets evaluate
```

## Install zsh and oh-my-zshell
```
apt-get install zsh
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

## Install Git LFS (for HuggingFace)
```
apt-get install git-lfs
git lfs install
```

## Clone the Transformers Library
```
git clone git@github.com:huggingface/transformers.git
```

## Start training!

```
base_name='vit-base'
dataset_name='mnist'

right_now=$(date +'%Y-%m-%d')
task_name=digit-classification

output_dir=/workspace/models/{base_model}/{dataset_name}/{task_name}/{right_now}

model_name=${dataset_name}-${task_name}
model_id=${model_name}-${right_now}

transformer_scripts=/workspace/transformers/examples/pytorch

train_batch_size=8
eval_batch_size=8

seed=42
wandb_project=${model_id}
logging_steps=100
run_img_cls_path=${transformer_scripts}/image-classification/run_image_classification.py

!python $run_img_cls_path \
    --dataset_name mnist                 \
    --output_dir             $output_dir \
    --overwrite_output_dir               \
    --remove_unused_columns False \
    --do_train \
    --do_eval \
    --push_to_hub \
    --hub_model_id $model_id \
    --hub_strategy all_checkpoints \
    --learning_rate 2e-5 \
    --num_train_epochs 5 \
    --per_device_train_batch_size $train_batch_size \
    --per_device_eval_batch_size $eval_batch_size \
    --logging_strategy steps \
    --save_steps 100 \
    --logging_steps $logging_steps \
    --save_strategy steps \
    --evaluation_strategy steps \
    --load_best_model_at_end True \
    --save_total_limit 3 \
    --seed $seed
```

