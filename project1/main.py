from PIL import Image
import numpy as np
import os
import sys


# Utils

def img_from_array(array):  # Transforma o array em imagem
    imagem = Image.fromarray(array, mode='RGB')
    return imagem


def img_to_array(array):
    return np.asarray(array)


def open_image(relative_path):
    print("Opening Image: {}".format(relative_path))
    try:
        f = Image.open(relative_path)
    except Exception as error:
        print(error)
        exit(1)
    

    print("Image Opened successfully.\n")
    return f


class ImageProcessor:
    def __init__(self, image):
        self.image = image
        self.img_array = img_to_array(self.image)
        self.height = len(self.img_array)
        self.width = len(self.img_array[0])

        print("Image Processor created")

    def show(self):
        self.image.show()
        print("Showing Image")

    def to_red_mono(self):
        print("Converting to Monocromatic Red Channel")
        img_copy = self.img_array.copy()
        for i in range(self.height):
            for j in range(self.width):
                img_copy[i][j][1] = 0
                img_copy[i][j][2] = 0
        return img_from_array(img_copy)


def main():
    f = open_image(sys.argv[1])
    img = ImageProcessor(f)
    img.show()

    print("Showing RED")
    red_image = img.to_red_mono()
    red_image.show()


if __name__ == "__main__":
    main()
