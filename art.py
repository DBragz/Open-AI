# Create a pixel image and display to window
import numpy as np
import matplotlib.pyplot as plt

# Create a pixel image
image = np.zeros((52, 85, 3), dtype=np.uint8)

# Draw a cool pixel gradient
for i in range(52):
    for j in range(85):
        image[i, j] = [i * 5, j * 3, (i + j) * 3]

# Add some text in a cool font and color
plt.text(40, 20, "Hello", fontsize=20, fontweight='bold', color='magenta')
plt.text(40, 25, "Oi", fontsize=20, fontweight='bold', color='cyan')

# Display the image
plt.imshow(image)
plt.axis('off')
plt.show()
