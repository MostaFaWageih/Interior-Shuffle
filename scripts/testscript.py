
import openai

openai.api_key = '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'

response = openai.Image.create_edit(
  image=open("/Users/asfandyarkhan/Desktop/Independent Study Repo/Interior-Shuffle/testing_pictures/house.png", "rb"),
  mask=open("/Users/asfandyarkhan/Desktop/Independent Study Repo/Interior-Shuffle/testing_pictures/converted_mask_origformfinalnewmidnightrgba.png", "rb"),
  prompt="put a blue couch with small white pillows",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']
print(image_url)