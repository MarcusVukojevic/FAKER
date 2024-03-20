import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from utils_funct import apply_fourier_transform
import os


lista_folders = [ "TestSet/dalle-mini_valid",  "TestSet/dalle_2", "TestSet/eg3d", "TestSet/progan_lsun", "TestSet/stable_diffusion_256", "TestSet/biggan_256", \
                  "TestSet/taming-transformers_class2image_ImageNet", "TestSet/latent-diffusion_noise2image_FFHQ",  "TestSet/glide_text2img_valid", "TestSet/stylegan3_r_ffhqu_1024x1024" \
                  "TestSet/stylegan3_t_ffhqu_1024x1024" ,  "TestSet/stylegan2_afhqv2_512x512",  "TestSet/biggan_512"]


#"TestSet/stylegan3_t_ffhqu_1024x1024"
fol = []
fol.append("TestSet/dalle-mini_valid")
fol.append("results/dalle-mini_valid_sr_drunet_color")
ris = []
rist = []
for i in range(2):
    folder = fol[i]
    lista_immagini = os.listdir(folder)

    risultato = 0
    tmp = []
    risultato_trans = 0
    try:
        for i, img in enumerate(lista_immagini):
            tmp.append(apply_fourier_transform(f'{folder}/{img}'))
            if(i==0):
                risultato=apply_fourier_transform(f'{folder}/{img}')
                #print("--------------------------> ",risultato)
            else:
                risultato+=apply_fourier_transform(f'{folder}/{img}')
        
        ris.append(risultato)
        rist.append(risultato_trans)

    except:
        pass


finale = tmp[0]

range_oggetti = set()
for i, img in enumerate(tmp):
    if i == 0:
        pass
    else:
        finale += img

risultato=ris[0]-ris[1]

plt.imshow(risultato, cmap='gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()
exit()