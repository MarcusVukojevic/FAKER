
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os
import numpy as np
from utils_funct import *

folder = "TestSet/stylegan2_afhqv2_512x512"
folder = "TestSet/biggan_512"


lista_immagini = os.listdir(folder)

tutte_le_magn = []


tmp = None
dio = None 

denoi  = None


cane = None


prova = None
res2 = None

for img in lista_immagini:

    dio = Image.open(f"{folder}/{img}").convert('L')
    res, denoise = residuo(f"{folder}/{img}")
    ress = adaptive_noise_filter(f"{folder}/{img}")

    denoi = denoise

    if tmp is None or res2 is None:
        tmp = res 
        res2 = ress
        prova = fft_da_array(tmp)
    else:
        tmp += res
        res2 += ress
        prova += fft_da_array(tmp)

avg_tmp = fft_da_array(tmp)



plot_images([ dio, tmp, res2, fft_da_array(res2)], "avg delle fft")
plot_images([avg_tmp, dio, denoi, tmp, scala_a_255(prova), res2], "avg delle fft")
