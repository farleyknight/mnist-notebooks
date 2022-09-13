from PIL import Image
import requests

#url = "https://i.pinimg.com/originals/47/e2/1d/47e21deacca0ef825933dfdbf33db1b4.jpg"
#image2 = Image.open(requests.get(url, stream=True).raw)
#print('image', image2)

from datasets import load_dataset
mnist = load_dataset("mnist")
image = mnist['train'][0]['image']
image = image.convert('RGB').resize((224, 224))

from transformers import AutoFeatureExtractor, AutoModelForImageClassification

extractor = AutoFeatureExtractor.from_pretrained("farleyknight/mnist-digit-classification-2022-09-04")

model = AutoModelForImageClassification.from_pretrained("farleyknight/mnist-digit-classification-2022-09-04")

inputs = extractor(images=image, return_tensors="pt")
outputs = model(**inputs)
logits = outputs["logits"]
predicted_class_idx = logits.argmax(-1).item()

print(model.config.id2label[predicted_class_idx])