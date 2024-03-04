import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from utils_funct import *


# Function to apply Fourier Transform to an image
def apply_fourier_transform(image):
    # Load the image
    # convert image to grayscale
    image_array = np.array(image)

    # Apply Fourier Transform
    f_transform = np.fft.fft2(image_array)
    f_shift = np.fft.fftshift(f_transform)

    # Get magnitude spectrum
    magnitude_spectrum = 20 * np.log(np.abs(f_shift))

    return magnitude_spectrum

def apply_transpose_fourier_transform(image):
    # Load the image
      # convert image to grayscale
    image_array = np.array(image)
    image_array = image_array.transpose()

    # Apply Fourier Transform
    f_transform = np.fft.fft2(image_array, )
    f_shift = np.fft.fftshift(f_transform)

    # Get magnitude spectrum
    magnitude_spectrum = 20 * np.log(np.abs(f_shift))
    return magnitude_spectrum



import os


folder = "TestSet/biggan_512"
folder ="TestSet/taming-transformers_class2image_ImageNet"
folder = "TestSet/stylegan2_afhqv2_512x512"
folder = "TestSet/stable_diffusion_256"
folder = "TestSet/glide_text2img_valid"
folder = "TestSet/dalle-mini_valid"

#"TestSet/stylegan3_t_ffhqu_1024x1024"
lista_immagini = os.listdir(folder)

risultato = 0
dio = []
risultato_trans = 0
for i, img in enumerate(lista_immagini):
    dio.append(apply_fourier_transform(residuo(f"{folder}/{img}")))
    if(i==0):
        risultato=apply_fourier_transform(residuo(f"{folder}/{img}"))
        risultato_trans=apply_transpose_fourier_transform(residuo(f"{folder}/{img}"))
        #print("--------------------------> ",risultato)
    else:
        risultato+=apply_fourier_transform(residuo(f"{folder}/{img}"))
        risultato_trans=apply_transpose_fourier_transform(residuo(f"{folder}/{img}"))


finale = dio[0]

range_oggetti = set()
for i, img in enumerate(dio):
    if i == 0:
        pass
    else:
        finale += img


plt.figure(figsize=(12, 6))
plt.subplot(121), plt.imshow(risultato_trans, cmap='gray')
plt.title('Trans'), plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(risultato, cmap='gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()
