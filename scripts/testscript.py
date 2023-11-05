
import openai


### REVERT TO THIS CODE IF THE CODE UNHIGHLIGHTED DOES NOT WORK

# # Placeholder values
# thing_to_put = "couch"
# color_of_thing = "blue"
# size_of_thing = "small"
# where_to_put = "living room corner"

# # Construct the prompt with placeholder values
# prompt_text = f"put a {color_of_thing} {thing_to_put} with {size_of_thing} white pillows in the {where_to_put}"

# response = openai.Image.create_edit(
#   image=open("/Users/asfandyarkhan/Desktop/Independent Study Repo/Interior-Shuffle/testing_pictures/house.png", "rb"),
#   mask=open("/Users/asfandyarkhan/Desktop/Independent Study Repo/Interior-Shuffle/testing_pictures/converted_mask_origformfinalnewmidnightrgba.png", "rb"),
#   prompt=prompt_text,
#   n=1,
#   size="1024x1024"
# )

# # Assuming the response structure has not changed
# image_url = response['data'][0]['url']
# print(image_url)




################################


import openai
import requests

def create_and_download_image(thing_to_put, color_of_thing, size_of_thing, image_path, mask_path):
    # Your OpenAI API key should be loaded from an environment variable or secure storage
    openai.api_key = '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'

    # Construct the prompt with placeholder values
    prompt_text = f"put a {size_of_thing} {color_of_thing} {thing_to_put}"

    # Call to the OpenAI API to edit the image
    response = openai.Image.create_edit(
        image=open(image_path, "rb"),
        mask=open(mask_path, "rb"),
        prompt=prompt_text,
        n=1,
        size="1024x1024"
    )
    
    # Close the file objects to avoid resource leaks
    image_file = open(image_path, "rb")
    mask_file = open(mask_path, "rb")
    image_file.close()
    mask_file.close()

    # Assuming the response structure has not changed
    image_url = response['data'][0]['url']

    # Download the image
    image_response = requests.get(image_url)
    if image_response.status_code == 200:
        # Assuming you want to save the image with a specific filename, you can do so here
        filename = "edited_image.png"
        with open(filename, 'wb') as f:
            f.write(image_response.content)
        return filename  # Return the filename where the image was saved
    else:
        raise Exception("Failed to download the image")

# Example usage
image_filename = create_and_download_image(
    "couch", "blue", "small",
    "/Users/asfandyarkhan/Desktop/Independent Study Repo/Interior-Shuffle/testing_pictures/house.png",
    "/Users/asfandyarkhan/Desktop/Independent Study Repo/Interior-Shuffle/testing_pictures/converted_mask_origformfinalnewmidnightrgba.png"
)

print(f"Image saved as {image_filename}")
