from PIL import Image

# Specify the desired size directly (width, height)
target_size = (1000, 667)  # For example, if your target size is 1000x667

# Load your mask image
mask_image_path = '/Users/asfandyarkhan/Desktop/Independent Study Repo/Interior-Shuffle/Test_Files/converted_mask.png'
mask_image = Image.open(mask_image_path)

# Resize the mask to match the target size
resized_mask = mask_image.resize(target_size, Image.ANTIALIAS)

# Save the resized mask image
resized_mask_path = '/Users/asfandyarkhan/Desktop/Independent Study Repo/Interior-Shuffle/Test_Files/resized_mask.png'
resized_mask.save(resized_mask_path)

print(f"Resized mask saved to {resized_mask_path}")
