import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.colors as colors


# MI FA LA FFT SULLE RIGHE SENZA SHIFT
def fft_righe(immagine):
    fft2_rows = np.fft.fft(immagine, axis=1)
    return fft2_rows

# MI FA LA FFT SULLE COLONNE SENZA SHIFT
def fft_colonne(immagine):
    fft2_columns = np.fft.fft(immagine, axis=0)
    return fft2_columns

# MI FA LA FFT SULLE RIGHE CON SHIFT
def fft_righe_shift(righe):
    wela_shift = np.fft.fftshift(fft_righe(righe), axes=(1,))
    magnitude_spectrum = 20 * np.log(np.abs(wela_shift))
    for i in range(len(magnitude_spectrum)):
        for j in range(len(magnitude_spectrum[i])):
            if(magnitude_spectrum[i][j] < 0):
                magnitude_spectrum[i][j] = 0

    return magnitude_spectrum

# MI FA LA FFT SULLE COLONNE CON SHIFT
def fft_colonne_shift(righe):
    wela_shift = np.fft.fftshift(fft_colonne(righe), axes=(0,))
    magnitude_spectrum = 20 * np.log(np.abs(wela_shift))

    for i in range(len(magnitude_spectrum)):
        for j in range(len(magnitude_spectrum[i])):
            if(magnitude_spectrum[i][j] < 0):
                magnitude_spectrum[i][j] = 0
    return magnitude_spectrum

# PRENDO UN ARRAY E FACCIO LA FFT + SHIFT --> SOLO MAGN
def fft_da_array(img):
    f_transform = np.fft.fft2(img)
    f_shift = np.fft.fftshift(f_transform)
    magnitude_spectrum = 20 * np.log(np.abs(f_shift))
    
    
    for i in range(len(magnitude_spectrum)):
        for j in range(len(magnitude_spectrum[i])):
            if(magnitude_spectrum[i][j] < 0):
                magnitude_spectrum[i][j] = 0

    return magnitude_spectrum


# PRENDO IL PATH DI UN'IMMAGINE E FACCIO LA FFT + SHIFT --> SOLO MAGN

def fft_da_immagine(img):
    image = Image.open(img).convert('L')
    image_array = np.array(image)

    f_transform = np.fft.fft2(image_array)
    f_shift = np.fft.fftshift(f_transform)
    magnitude_spectrum = (np.abs(f_shift))
    
    for i in range(len(magnitude_spectrum)):
        for j in range(len(magnitude_spectrum[i])):
            if(magnitude_spectrum[i][j] < 0):
                magnitude_spectrum[i][j] = 0
    return magnitude_spectrum


# PRENDO UN ARRAY E FACCIO LA FFT + SHIFT + MAGNITUDE + PHASE --> mi restituisce un'immagine rgb a colori con magnitude e fase combinati

def fft_da_array_colorized(img):
    f_transform = np.fft.fftshift(np.fft.fft2(img))
    magnitude = np.abs(f_transform)
    phase = np.angle(f_transform)

    hue = (phase + np.pi) / (2 * np.pi)  # Normalize phase to 0-1
    saturation = np.ones_like(hue)  # Full saturation
    value = magnitude / 255  # Use scaled magnitude for value
    hsv_image = np.stack([hue, saturation, value], axis=-1)
    rgb_image = colors.hsv_to_rgb(hsv_image)

    return rgb_image

# PRENDO UN'IMMAGINE E FACCIO LA FFT + SHIFT + MAGNITUDE + PHASE --> mi restituisce un'immagine rgb a colori con magnitude e fase combinati

def fft_da_array_colorized_da_immagine(img):
    image = Image.open(img).convert('L')
    image_array = np.array(image)
    
    f_transform = np.fft.fftshift(np.fft.fft2(image_array))
    magnitude = np.abs(f_transform)
    phase = np.angle(f_transform)

    hue = (phase + np.pi) / (2 * np.pi)  # Normalize phase to 0-1
    saturation = np.ones_like(hue)  # Full saturation
    value = magnitude / 255  # Use scaled magnitude for value
    hsv_image = np.stack([hue, saturation, value], axis=-1)
    rgb_image = colors.hsv_to_rgb(hsv_image)

    return rgb_image


# PLOTTO LE IMMAGINI DATE UNA LISTA DI IMMAGINI E TITOLI

def plot_images(lista_immagini, lista_titoli):

    plt.figure(figsize=(12, 6))
    
    for i in range(len(lista_immagini)):
        plt.subplot(1, len(lista_immagini), i + 1)
        plt.imshow(lista_immagini[i], cmap='gray', vmin=0, vmax=255)
        plt.title(f'{lista_titoli[i]}')
        plt.xticks([]), plt.yticks([])
        
    plt.show()


def scala_a_255(magnitude):
    magnitude -= magnitude.min()
    magnitude = magnitude / magnitude.max()
    magnitude *= 255

    return magnitude.astype(np.uint8)

from scipy.fftpack import fft2, ifft2
from scipy.ndimage import gaussian_filter

def compute_prnu(img, noise_std=0, filter_std=1.0):
    """
    Compute the PRNU pattern of an image using a Wiener filter.

    :param image: Input image (2D numpy array).
    :param noise_std: Standard deviation of the noise.
    :param filter_std: Standard deviation for Gaussian filter.
    :return: PRNU pattern.
    """
    image = Image.open(img).convert('L')
    image_array = np.array(image)
    # Apply a Gaussian filter (denoising)
    denoised_image = gaussian_filter(image_array, filter_std)

    # Compute the residual (noise)
    residual = image_array - denoised_image

    # Apply Wiener filter in the frequency domain
    image_fft = fft2(residual)
    psd = np.abs(image_fft)  # Power spectral density
    wiener_filter = psd / (psd + noise_std ** 2)
    prnu_pattern = np.real(ifft2(image_fft * wiener_filter))

    return prnu_pattern



def residuo(img, deviazione=1.0):
    

    image = Image.open(img).convert('L')
    image_array = np.array(image)
   

    denoised_image = gaussian_filter(image_array, deviazione)

    # Compute the residual (noise)
    residual = image_array - denoised_image

    return np.array(residual)

# suca

def create_image_with_moving_block(size, block_size, move_distance):
    # Create an image with a black background
    image = np.zeros((size, size), dtype=np.uint8)

    # Calculate the end position of the block, ensuring it stays within the image boundaries
    end_x = min(size, block_size + move_distance)
    end_y = min(size, block_size + move_distance)

    # Place the white block
    image[move_distance:end_y, move_distance:end_x] = 255

    return image


import cv2
import numpy as np

def adaptive_noise_filter(image_path):
    # Read the image
    image = cv2.imread(image_path, 0)  # 0 to read image in grayscale

    # Estimate the local mean and variance
    mean = cv2.blur(image, (3, 3))
    mean_sq = cv2.blur(image**2, (3, 3))
    variance = mean_sq - mean**2

    # Estimate the noise variance
    noise_variance = np.mean(np.var(image))

    # Apply the adaptive Wiener filter
    with np.errstate(divide='ignore', invalid='ignore'):
        result = mean + np.where(variance == 0, 0, 
                                 (variance - noise_variance) / variance) * (image - mean)
        # Where variance is zero, output mean instead of dividing by zero
        result[variance == 0] = mean[variance == 0]

    # The estimated noise is the difference between the original and the result
    noise = image - result

    return noise.astype(np.uint8)

