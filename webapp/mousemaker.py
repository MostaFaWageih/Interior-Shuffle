import tkinter as tk
from PIL import Image, ImageTk, ImageDraw

class ImageEraser:
    def __init__(self, path):
        self.path = path
        self.root = tk.Tk()
        self.root.title('Image Eraser')

        # Load the image
        self.image = Image.open(self.path)
        self.image = self.image.convert("RGBA")  # Convert to RGBA
        self.tk_image = ImageTk.PhotoImage(self.image)

        # Create a drawing canvas
        self.canvas = tk.Canvas(self.root, width=self.tk_image.width(), height=self.tk_image.height())
        self.canvas.pack()

        # Display image on the canvas
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)

        # Bind mouse events to methods
        self.canvas.bind("<B1-Motion>", self.erase)

        # Drawing configuration
        self.draw = ImageDraw.Draw(self.image)
        self.eraser_size = 25

        self.root.mainloop()

    def erase(self, event):
        x1, y1 = (event.x - self.eraser_size), (event.y - self.eraser_size)
        x2, y2 = (event.x + self.eraser_size), (event.y + self.eraser_size)

        # Draw transparent ellipse
        self.draw.ellipse([x1, y1, x2, y2], fill=(255, 255, 255, 0))

        # Update display
        self.tk_image = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)

    def save_image(self, output_path):
        self.image.save(output_path, 'PNG')
