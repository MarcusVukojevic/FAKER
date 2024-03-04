import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Function to apply Fourier Transform to an image
def apply_fourier_transform(image_path):
    # Load the image
    image = Image.open(image_path).convert('L')  # convert image to grayscale
    image_array = np.array(image)

    # Apply Fourier Transform
    f_transform = np.fft.fft2(image_array)
    f_shift = np.fft.fftshift(f_transform)

    # Get magnitude spectrum
    magnitude_spectrum = 20 * np.log(np.abs(f_shift))

    return magnitude_spectrum

def apply_transpose_fourier_transform(image_path):
    # Load the image
    image = Image.open(image_path).convert('L')  # convert image to grayscale
    image_array = np.array(image)
    image_array = image_array.transpose()

    # Apply Fourier Transform
    f_transform = np.fft.fft2(image_array, )
    f_shift = np.fft.fftshift(f_transform)

    # Get magnitude spectrum
    magnitude_spectrum = 20 * np.log(np.abs(f_shift))
    return magnitude_spectrum


# You would call the function with the path to your image like this:
# apply_fourier_transform('path_to_your_image.jpg')
#apply_fourier_transform('TestSet/biggan_512/biggan_004_917321.png')



import os

folder = "TestSet/dalle-mini_valid"
folder = "TestSet/dalle_2"
folder = "TestSet/eg3d" 
folder = "TestSet/progan_lsun" 
folder = "TestSet/stable_diffusion_256"
folder = "TestSet/biggan_256"
folder ="TestSet/taming-transformers_class2image_ImageNet"
folder = "TestSet/latent-diffusion_noise2image_FFHQ"
folder = "TestSet/glide_text2img_valid"
folder = "TestSet/stylegan3_r_ffhqu_1024x1024"
folder = "TestSet/stylegan3_t_ffhqu_1024x1024"
folder = "TestSet/stylegan2_afhqv2_512x512"
folder = "TestSet/biggan_512"

#"TestSet/stylegan3_t_ffhqu_1024x1024"
lista_immagini = os.listdir(folder)

risultato = 0
dio = []
risultato_trans = 0
for i, img in enumerate(lista_immagini):
    dio.append(apply_fourier_transform(f'{folder}/{img}'))
    if(i==0):
        risultato=apply_fourier_transform(f'{folder}/{img}')
        risultato_trans=apply_transpose_fourier_transform(f'{folder}/{img}')
        #print("--------------------------> ",risultato)
    else:
        risultato+=apply_fourier_transform(f'{folder}/{img}')
        risultato_trans=apply_transpose_fourier_transform(f'{folder}/{img}')


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
exit()

plt.figure(figsize=(12, 6))
plt.imshow(risultato, cmap='gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])

# Show the plots
plt.show()


print(risultato.shape)
print(len(risultato))
print(len(risultato[0]))

if(2==2):
    budelino = 1
    budelino2 = 20
    for j in range(len(risultato)):
        for k in range(int(len(risultato[j])/2) - budelino, int(len(risultato[j])/2)+ budelino):
                risultato[j][k] = 0
        if (j > int(len(risultato)/2 -budelino)) and (j < int(len(risultato)/2 + budelino)):
            for k in range(int(len(risultato[j]))):
                risultato[j][k] = 0
        if (j > int(len(risultato)/2 -budelino2)) and (j < int(len(risultato)/2 + budelino2)):
            for k in range(int(len(risultato[j])/2) - budelino2, int(len(risultato[j])/2)+ budelino2):
                risultato[j][k] = 0
        #for k in range(int(len(risultato[j])/2),int(len(risultato[j]))):
        #    risultato[j][k] = 0

if(1==1):
    for j in range(len(risultato)):
        for k in range(len(risultato[j])):
            if(risultato[j][k] >= 105000):
                risultato[j][k] = 0



plt.figure(figsize=(12, 6))
plt.imshow(risultato, cmap='gray',vmin=0, vmax=100000)
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()