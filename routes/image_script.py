import os
import openai
import requests

openai.api_key = os.getenv("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")
openai.Model.list()
# openai.api_key = os.environ["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"]

response = openai.Image.create_edit(
    image=open("/dalle/image.png", "rb"),
    mask=open("/dalle/mask.png", "rb"),
    prompt="An indoor lounge area with a brown dog swimming in the pool",
    n=1,
    size="256x256"
)

url = response["data"][0]["url"]

data = requests.get(url).content

f = open('output/img.png','wb')

f.write(data)
f.close()
