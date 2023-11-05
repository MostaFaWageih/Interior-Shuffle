
import tkinter as tk
from PIL import Image, ImageTk, ImageDraw

# Path to your image
image_path = '/Users/student/Desktop/PhotoEditor/example_input/house.jpg'

class ImageEraser:
    def __init__(self, path):
        self.root = tk.Tk()
        self.root.title('Image Eraser')

        # Load the image
        self.image = Image.open(path)
        self.image = self.image.convert("RGBA")  # Convert to RGBA to add an alpha channel
        self.tk_image = ImageTk.PhotoImage(self.image)

        # Create a drawing canvas
        self.canvas = tk.Canvas(self.root, width=self.tk_image.width(), height=self.tk_image.height())
        self.canvas.pack()

        # Display image on the canvas
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)

        # Bind mouse events to methods
        self.canvas.bind("<B1-Motion>", self.erase)

        # Keep track of the drawing
        self.draw = ImageDraw.Draw(self.image)

        # Set the eraser size (radius of the circle)
        self.eraser_size = 25

        self.root.mainloop()

    def erase(self, event):
        # Get mouse position
        x1, y1 = (event.x - self.eraser_size), (event.y - self.eraser_size)
        x2, y2 = (event.x + self.eraser_size), (event.y + self.eraser_size)

        # Draw transparent ellipse on the image
        self.draw.ellipse([x1, y1, x2, y2], fill=(255, 255, 255, 0))

        # Update the display
        self.tk_image = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)

    def save_image(self):
        # Save the edited image
        self.image.save('edited_image.png', 'PNG')
        print("Image saved as 'edited_image.png'")

# Create an instance of the ImageEraser with your image path
eraser = ImageEraser(image_path)
eraser.save_image()
