from PIL import Image

# Open the image file
img = Image.open('/Users/asfandyarkhan/Desktop/Independent Study Repo/Interior-Shuffle/Test_Files/test_interior_1_preview_rev_1.png')

# Convert the image to 'RGBA'
img = img.convert('RGBA')

# Save the converted image
img.save('/Users/asfandyarkhan/Desktop/Independent Study Repo/Interior-Shuffle/Test_Files/converted_mask.png')
