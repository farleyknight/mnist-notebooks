import requests
import json
import requests

model_path = "farleyknight/mnist-digit-classification-2022-09-04"
API_TOKEN  = "" # TODO: Add the token here. It's in digit-recognition-app
headers    = {"Authorization": f"Bearer {API_TOKEN}"}
API_URL    = f"https://api-inference.huggingface.co/models/{model_path}"

# TODO: Using this snippet of code, figure out how to do inference
# on several images from the load_dataset("mnist") dataset
def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))

data = query("cats.jpg")