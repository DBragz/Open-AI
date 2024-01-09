# Create a pixel image and display to window
import numpy as np
import matplotlib.pyplot as plt

# Create a pixel image
image = np.zeros((52, 85, 3), dtype=np.uint8)

# Draw a red circle
image[10:50, 10:50, 0] = 255

# Display the image
plt.imshow(image)
plt.axis('off')
plt.show()
