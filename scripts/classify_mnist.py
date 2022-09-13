from PIL import Image
import requests

#url = "https://i.pinimg.com/originals/47/e2/1d/47e21deacca0ef825933dfdbf33db1b4.jpg"
#image2 = Image.open(requests.get(url, stream=True).raw)
#print('image', image2)

from datasets import load_dataset
mnist = load_dataset("mnist")

def convert_image(index):    
    return mnist['train'][index]['image'].convert('RGB').resize((224, 224))

from transformers import AutoFeatureExtractor, AutoModelForImageClassification

extractor = AutoFeatureExtractor.from_pretrained("farleyknight/mnist-digit-classification-2022-09-04")

model = AutoModelForImageClassification.from_pretrained("farleyknight/mnist-digit-classification-2022-09-04")


def run_prediction(images):
    assert type(images) == list
    
    import time

    start = time.time()

    inputs = extractor(images=images, return_tensors="pt")
    outputs = model(**inputs)
    logits = outputs["logits"]
    results = []
    for pred in logits:
        result = pred.argmax(-1).item()
        results.append(result)
        
    end = time.time()

    pred_time = end - start
    print('prediction time', pred_time)
    print('prediction time per image', pred_time / len(images))
    for result in results:
        print(model.config.id2label[result])

images = []
for i in range(10):
    images.append(convert_image(i))
        
run_prediction(images)