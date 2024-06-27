import cv2
import matplotlib.pyplot as plt
# Read image
img = cv2.imread('image try 1.png')
cv2.imshow('image',img)
input('Press a to exit')
# plt.imshow(img)
# input('Press ENTER to exit')
# Print image dimensions
# input('Press ENTER to exit')
print('Image Dimensions :', img.shape)

# import numpy as np

# def create_grid(image, rows, cols):
#     # Get image dimensions
#     height, width, _ = image.shape

#     # Calculate block size
#     block_height = height // rows
#     block_width = width // cols

#     # Draw horizontal lines
#     for i in range(1, rows):
#         cv2.line(image, (0, i * block_height), (width, i * block_height), (0, 255, 0), 2)

#     # Draw vertical lines
#     for j in range(1, cols):
#         cv2.line(image, (j * block_width, 0), (j * block_width, height), (0, 255, 0), 2)

#     return image

# def separate_image(image, rows, cols):
#     # Get image dimensions
#     height, width, _ = image.shape

#     # Calculate block size
#     block_height = height // rows
#     block_width = width // cols

#     # Separate the image into blocks
#     blocks = []
#     for i in range(rows):
#         for j in range(cols):
#             block = image[i * block_height: (i + 1) * block_height, j * block_width: (j + 1) * block_width]
#             blocks.append(block)

#     return blocks

# Load your image
# image_path = 'path/to/your/image.jpg'
# original_image = cv2.imread(image_path)

# Specify the number of rows and columns in the grid
# num_rows = 3
# num_cols = 3

# # Create a grid overlay on the original image
# image_with_grid = create_grid(img.copy(), num_rows, num_cols)

# # Display the image with the grid
# # cv2.imshow(image_with_grid)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()

# # Separate the image into blocks
# image_blocks = separate_image(img, num_rows, num_cols)

# # Display the individual blocks (for demonstration purposes)
# # for i, block in enumerate(image_blocks):
# #     cv2.imshow(block)
# #     cv2.waitKey(0)
# #     cv2.destroyAllWindows()
