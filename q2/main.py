import numpy as np
import cv2
import os

def bit_plane_slicing(img):
    bit_planes = []
    for i in range(8):
        bit_planes.append((img >> i) & 1)
    return bit_planes

def compress_image_by_bit_planes(bit_planes, selected_planes):
    compressed_img = np.zeros_like(bit_planes[0], dtype=np.uint8)
    for i in selected_planes:
        compressed_img += (bit_planes[i] << i)
    return compressed_img


input_image_path = 'figs/cow.jpg'
compressed_image_path = 'figs/cow-compress.jpg'

original_img = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)

bit_planes = bit_plane_slicing(original_img)

selected_planes = [7]

compressed_img = compress_image_by_bit_planes(bit_planes, selected_planes)

original_size = cv2.imwrite(input_image_path, original_img)
compressed_size = cv2.imwrite(compressed_image_path, compressed_img)

print("original size:   ", os.path.getsize(input_image_path))
print("compressed size: ", os.path.getsize(compressed_image_path))
