import numpy as np
import matplotlib.pyplot as plt
import pywt
from PIL import Image

# Function to apply Wavelet Transform to an image and visualize the result
def apply_wavelet_transform(image_path):
    # Load the image
    image = Image.open(image_path).convert('L')  # convert image to grayscale for simplicity
    image_array = np.array(image)

    # Apply Wavelet Transform using PyWavelets
    coeffs = pywt.dwt2(image_array, 'sym2')
    cA, (cH, cV, cD) = coeffs

    # Visualizing the results
    fig = plt.figure(figsize=(12, 3))

    titles = ['Approximation', ' Horizontal detail',
              'Vertical detail', 'Diagonal detail']
    for i, a in enumerate([cA, cH, cV, cD]):
        ax = fig.add_subplot(1, 4, i + 1)
        ax.imshow(a, interpolation="nearest", cmap=plt.cm.gray)
        ax.set_title(titles[i], fontsize=10)
        ax.set_xticks([])
        ax.set_yticks([])

    fig.tight_layout()
    plt.show()

# The path to the provided image
image_path = 'wela.png'

# Apply the Wavelet Transform to the image and display the results
apply_wavelet_transform(image_path)
