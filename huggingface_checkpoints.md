One note about HuggingFace checkpoints:
* They explicitly state in the documentation that the trainer's checkpoints do NOT include the optimizer state. 
* That means that even if you can resume from a checkpoint, you might not get the results you expect.