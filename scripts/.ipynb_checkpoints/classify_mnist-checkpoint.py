from PIL import Image
import requests

url = "https://i.pinimg.com/originals/47/e2/1d/47e21deacca0ef825933dfdbf33db1b4.jpg"

image = Image.open(requests.get(url, stream=True).raw)

print('image', image)

from transformers import AutoFeatureExtractor, AutoModelForImageClassification

extractor = AutoFeatureExtractor.from_pretrained("farleyknight/mnist-digit-classification-2022-09-04")

model = AutoModelForImageClassification.from_pretrained("farleyknight/mnist-digit-classification-2022-09-04")

inputs = extractor(images=image, return_tensors="pt")
outputs = model(**inputs)
logits = outputs["logits"]
predicted_class_idx = logits.argmax(-1).item()

print(model.config.id2label[predicted_class_idx])