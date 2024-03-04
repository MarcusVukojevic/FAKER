import numpy as np
import matplotlib.pyplot as plt

# Define image dimensions
width = 256
height = 256

# Create a grid of coordinates
x = np.linspace(0, 2 * np.pi, width)
y = np.linspace(0, 2 * np.pi, height)

x, y = np.meshgrid(x, y)

# Define parameters for the cosine pattern
frequency_x = 5  # Adjust this to control horizontal repetitions
frequency_y = 0  # Adjust this to control vertical repetitions
amplitude = 127  # Adjust this to control the amplitude (brightness) of the pattern

# Generate the cosine pattern
cosine_pattern = amplitude * np.cos(frequency_x * x) * np.cos(frequency_y * y)

# Convert the pattern to uint8 (0-255 range) for visualization
cosine_pattern_uint8 = cosine_pattern.astype(np.uint8)

# Display the pattern using matplotlib
plt.imshow(cosine_pattern_uint8, cmap='gray')
plt.title("Cosine Repeated Pattern")
plt.axis('off')
plt.show()

# Save the pattern as an image (optional)
# Uncomment the following line to save the image
# plt.imsave("cosine_pattern.png", cosine_pattern_uint8, cmap='gray')
