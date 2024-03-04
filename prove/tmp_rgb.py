import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Function to apply Fourier Transform to each color channel of an RGB image
def apply_fourier_transform_rgb(image_path):
    # Load the image
    image = Image.open(image_path)
    # Convert image to numpy array
    image_array = np.array(image)

    # Initialize a list to hold the magnitude spectrums for each channel
    magnitude_spectrums = []

    # Apply Fourier Transform to each channel
    for i in range(3): # Loop through the color channels
        # Apply the Fourier transform
        f_transform = np.fft.fft2(image_array[:, :, i])
        f_shift = np.fft.fftshift(f_transform)
        
        # Calculate the magnitude spectrum
        magnitude_spectrum = 20 * np.log(np.abs(f_shift) + 1) # Adding 1 to avoid log(0)
        magnitude_spectrums.append(magnitude_spectrum)

    # Plotting the original image and the magnitude spectrum for each channel
    plt.figure(figsize=(10, 10))

    # Plot the original image
    plt.subplot(221), plt.imshow(image), plt.title('Input Image'), plt.axis('off')

    # Plot the magnitude spectrum of each channel
    plt.subplot(222), plt.imshow(magnitude_spectrums[0], cmap='gray'), plt.title('Red Channel Magnitude Spectrum'), plt.axis('off')
    plt.subplot(223), plt.imshow(magnitude_spectrums[1], cmap='gray'), plt.title('Green Channel Magnitude Spectrum'), plt.axis('off')
    plt.subplot(224), plt.imshow(magnitude_spectrums[2], cmap='gray'), plt.title('Blue Channel Magnitude Spectrum'), plt.axis('off')

    # Display the plots
    plt.show()

# The path to the provided image
image_path = 'wela.png'

# Apply the Fourier Transform to the RGB image and display the results
apply_fourier_transform_rgb(image_path)
