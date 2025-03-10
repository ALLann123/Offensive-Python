from PIL import Image
import numpy as np

# Open image
img = Image.open("red.png")

# Convert to NumPy array
data = np.array(img)

# Extract red channel
red_channel = data[:, :, 0]  # Red is the first channel in (R, G, B)

# Convert to text
decoded_text = "".join([chr(pixel) for row in red_channel for pixel in row if pixel > 32])
print(decoded_text)
