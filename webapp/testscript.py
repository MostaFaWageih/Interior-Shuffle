import openai
import requests
import datetime
import os

# Set your OpenAI API key in an environment variable for security
openai.api_key = "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"

def create_and_download_image(thing_to_put, color_of_thing, size_of_thing, theme, image_path, mask_path):
    prompt_text = f"put a {size_of_thing} {color_of_thing} {thing_to_put} with a {theme} theme"

    with open(image_path, "rb") as image_file, open(mask_path, "rb") as mask_file:
        response = openai.Image.create_edit(
            image=image_file,
            mask=mask_file,
            prompt=prompt_text,
            n=1,
            size="1024x1024"
        )

    image_url = response['data'][0]['url']
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"edited_image_{timestamp}.png"
    save_dir = "generated_images"
    os.makedirs(save_dir, exist_ok=True)
    save_path = os.path.join(save_dir, filename)

    image_response = requests.get(image_url)
    if image_response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(image_response.content)

    return save_path
