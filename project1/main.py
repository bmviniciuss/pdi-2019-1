from PIL import Image
import numpy as np
import os
import sys


# Utils
def img_from_array(array):  # Transforma o array em imagem
    """Transforma uma array em um Objeto Image"""
    imagem = Image.fromarray(array, mode='RGB')
    return imagem


def img_to_array(array):
    """Transforma uma Image em array usando numpy"""
    return np.asarray(array)


def open_image(relative_path):
    """Função que carrega uma imagem e retorna um objeto Image"""
    print("Opening Image: {}".format(relative_path))
    try:
        f = Image.open(relative_path)
    except Exception as error:
        print(error)
        exit(1)

    print("Image Opened successfully.\n")
    return f


class ImageProcessor:
    """Classe processa a imagem"""

    def __init__(self, image):
        """Inicia a classe com uma imagem, transforma para array e pega as dimensoes dela"""
        self.image = image
        self.img_array = img_to_array(self.image)
        self.height = len(self.img_array)
        self.width = len(self.img_array[0])

        print("Image Processor created")

    def show(self):
        """Exibe uma imagem"""
        self.image.show()
        print("Showing Image")

    def to_red_mono(self):
        """COnverte uma Imagem RGB para escala monocromatica no canal R"""
        print("Converting to Monocromatic Red Channel")
        img_copy = self.img_array.copy()
        for i in range(self.height):
            for j in range(self.width):
                img_copy[i][j][1] = 0
                img_copy[i][j][2] = 0
        return img_from_array(img_copy)


def main():
    f = open_image(sys.argv[1])  # abre a imagem que foi definidade na execução
    img = ImageProcessor(f)  # cria a classe com a imagem aberta
    img.show()  # mostra imagem original

    print("Showing RED")
    red_image = img.to_red_mono()  # gera uma imagem monocormatica em R
    red_image.show()  # mostra essa imagem

# FAZER:
# - Migrar para Jupyter


if __name__ == "__main__":
    main()
