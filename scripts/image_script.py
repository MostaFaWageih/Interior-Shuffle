import os
import openai
import requests
from datetime import datetime

# Set your API key securely

openai.api_key = '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'


# Ensure you have your own image and mask image in the same directory as this script
# or provide the full path to the images
image_path = "/Users/asfandyarkhan/Desktop/Independent Study Repo/Interior-Shuffle/testing_pictures/resized_main_44notmask4imagemidnight.png"  # Update this path
mask_path = "/Users/asfandyarkhan/Desktop/Independent Study Repo/Interior-Shuffle/testing_pictures/resized_main_444imagemidnight.png"    # Update this path

response = openai.Image.create_edit(
    image=open(image_path, "rb"),
    mask=open(mask_path, "rb"),
    prompt="Add a blue sofa where the mask is ",  # Update prompt as needed
    n=1,
    size="256x256"
)

# Obtain the URL of the generated image
url = response["data"][0]["url"]

# Download the image content
data = requests.get(url).content

# Save the downloaded image to your system
output_directory = 'output'
current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
os.makedirs(output_directory, exist_ok=True)  # Create output directory if it does not exist
output_path = os.path.join(output_directory, f'edited_image_{current_time}.png')

with open(output_path, 'wb') as f:
    f.write(data)

print(f"Image saved to {output_path}")


