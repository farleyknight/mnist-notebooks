# GitHub setup (still somewhat manual)

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

# Hugging Face Login (might be manual? can we automate?)

## Login to HuggingFace

```bash
pip install huggingface_hub
huggingface-cli login
```
