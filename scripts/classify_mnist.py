import torch
import time
import json
from os.path import exists

from transformers import AutoFeatureExtractor, AutoModelForImageClassification

from datasets import load_dataset
mnist = load_dataset("mnist")

def convert_image(index):    
    return mnist['train'][index]['image'].convert('RGB').resize((224, 224))

extractor = AutoFeatureExtractor.from_pretrained("farleyknight/mnist-digit-classification-2022-09-04")
model = AutoModelForImageClassification.from_pretrained("farleyknight/mnist-digit-classification-2022-09-04")

def verify_prediction(output, args):
    filename = output
    # verify filename exists    
    if not exists(filename):
        return False

    # unpack args
    start = args.get('start', 0)
    end = args.get('end', 9)
    
    # open up the file, and make sure there are (end-start) entries in it
    with open(filename) as f:
        records = json.loads(f.read())
    return len(records) == (end - start)

def run_prediction(args):
    start = args.get('start', 0)
    end   = args.get('end', 9)
    output_dir = args.get('output_dir', 'data/classify_mnist/')
    index_range = range(start, end+1)
    images = [convert_image(i) for i in index_range]
    
    start = time.time()

    inputs = extractor(images=images, return_tensors="pt")
    outputs = model(**inputs)
    logits = outputs["logits"]
    results = {}
    for logit, index in zip(logits, index_range):
        result = torch.nn.functional.softmax(logit, dim=0)
        results[index] = result.tolist()
        
    end = time.time()

    pred_time = end - start
    print('prediction time', pred_time)
    print('prediction time per image', pred_time / len(images))
    
    file_name = f"start_{start}_end_{end}.json"
    full_file_name = output_dir + file_name
    with open(full_file_name, 'w') as f:
        f.write(json.dumps(result))
    return full_file_name
