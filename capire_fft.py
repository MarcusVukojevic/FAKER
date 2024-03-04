from utils_funct import * 
import numpy as np
import matplotlib.pyplot as plt


img = np.full((512,512), 1, dtype=np.float64)
#print(len(img))
img = img.transpose()


valor = set()
#for j in range(len(img)):
#    for k in range(len(img)):
#        img[j][k] = k % 255
#        valor.add(k)

#print(valor)
'''

for j in range(len(img)):
    for k in range(int(len(img[j])/3), int(len(img[j])*2/3)):
            img[j][k] = 85
    for k in range(int(len(img[j])*2/3), int(len(img[j]))):
            img[j][k] = 250

'''
'''
for j in range(len(img)):
    for k in range(len(img[j])):
            if(k<=j):
                img[j][k] = 10


for j in range(len(img)):
    if j > len(img)/2 - len(img)/6 and j < len(img)/2 + len(img)/6:
        for k in range(len(img[j])):
            if(k >= j/2):
                img[j][k] = 255

for j in range(len(img)):
    for k in range(len(img[j])):
        if(k == j/20):
            img[j][k] = 255
'''
              



for j in range(len(img)):
    if j > len(img)/3 and j < len(img)*2/3:
        for k in range(len(img[j])):
            if(k > len(img)/3 and k <  len(img)*2/3):
                img[j][k] = 255

        

#img = cosine_func_image()
plot_images([fft_righe_shift(img), fft_colonne_shift(img), fft_da_array(img), img], ["riga", "colonna", "fft2", "img"])
exit()

wela = fft_da_array(img)
for i in wela:
    for j in i:
        valor.add(j)
print("wela")
print(valor)

plot_images([fft_da_array(img), fft_da_array(img.transpose()), img, img.transpose()], ["fft", "fft_trans", "img", "img.trans"])