from filtri import *
import os
from skimage import io
import matplotlib.pyplot as plt



folder = "TestSet/biggan_512"

lista_immagini = os.listdir(folder)


dio = Image.open(f"{folder}/{lista_immagini[0]}").convert('L')

prova = wavelet_denoise(dio)
dio =  np.clip(dio, 0, 1)

plt.imshow(dio - (dio-prova))
plt.show()