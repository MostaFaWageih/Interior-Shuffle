from PIL import Image

# Open the image file
img = Image.open('/Users/asfandyarkhan/Desktop/Independent Study Repo/Interior-Shuffle/testing_pictures/resized_main_44imagemidnight.png')

# Convert the image to 'RGBA'
img = img.convert('RGBA')

# Save the converted image
img.save('/Users/asfandyarkhan/Desktop/Independent Study Repo/Interior-Shuffle/testing_pictures/converted_image_origformfinalnewmidnightrgbamidmight.png')

