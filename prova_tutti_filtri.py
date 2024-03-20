import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from filtri import median_filtering, bilateral_filtering, adaptive_noise_filter, gaussian_filter, wavelet_denoise


cartella_ori = "TestSet/biggan_512"
cartella_ori = "TestSet/dalle-mini_valid"

lista_immagini = os.listdir(cartella_ori)

os.chdir("FILTRI")
lista_nomi_cartelle = ["median", "bilateral", "adaptive", "gaussian", "wavelet"]

for i in lista_nomi_cartelle:
    noise = []
    print(i)
    for img in lista_immagini:
        if i == "median":
            residuo = median_filtering(f"../{cartella_ori}/{img}")
        elif i == "bilateral":
            residuo = bilateral_filtering(f"../{cartella_ori}/{img}")
        elif i == "adaptive":
            residuo = adaptive_noise_filter(f"../{cartella_ori}/{img}")
        elif i == "gaussian":
            residuo = gaussian_filter(str(f"../{cartella_ori}/{img}"))
        elif i == "wavelet":
            residuo = wavelet_denoise(f"../{cartella_ori}/{img}")
        noise.append(residuo)

    media_rumore_complessiva = np.mean(noise, axis=0)

    f_transform = np.fft.fft2(media_rumore_complessiva)
    f_shift = np.fft.fftshift(f_transform)
    magnitude_spectrum = 20 * np.log(np.abs(f_shift))


    plt.imshow(magnitude_spectrum)
    plt.title(f'{i} Filter'), plt.xticks([]), plt.yticks([])
    plt.savefig(f'dalle_mini_{i}.png')
        

        

        
   

