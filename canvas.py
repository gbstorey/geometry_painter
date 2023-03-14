import numpy as np
from PIL import Image


class Canvas:
    def __init__(self, width: int, height: int, color: list[int, int, int]):
        """Creates the background of the image with assigned width, height, and color.

        :param width: Pixel width of the image/background.
        :param height: Pixel height of the image/background.
        :param color: Background color of canvas (e.g. [255, 255, 255])
        """
        self.width = width
        self.height = height
        self.color = color
        # Create a numpy array of zeros
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        # Set every pixel to the specified color
        self.data[:] = self.color

    def make(self, image_path: str):
        """Converts the current array into an image file and saves it."""
        img = Image.fromarray(self.data, 'RGB')
        img.save(image_path)
