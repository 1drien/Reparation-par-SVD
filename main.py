import numpy as np
from matplotlib import pyplot as plt
from scipy.linalg import svd
bw_image_file_path = "cheval-abime2-nb.png"
color_image_file_path = "cheval-abime2.png"
mask_file_path = "cheval-abime2-mask.png"

def read_image(file_path):
    image = plt.imread(file_path)
    return image

def restore_image(image, mask, rank):
    U, sigma, Vt = svd(image)
    U_k = U[:, :rank]
    sigma_k = np.diag(sigma[:rank])
    Vt_k = Vt[:rank, :]
    image_restored = U_k @ sigma_k @ Vt_k
    return np.where(mask, image_restored, image)

bw_image_file_path = "cheval-abime2-nb.png"
color_image_file_path = "cheval-abime2.png"
mask_file_path = "cheval-abime2-mask.png"

bw_image = read_image(bw_image_file_path)
color_image = read_image(color_image_file_path)
mask = read_image(mask_file_path)

mask = (mask > 0)

rank = 50

bw_image_restored = restore_image(bw_image, mask, rank)

color_image_restored = np.zeros_like(color_image)
for channel in range(3):
    color_image_restored[:, :, channel] = restore_image(color_image[:, :, channel], mask, rank)

plt.figure()
plt.imshow(bw_image, cmap="gray")
plt.title("Original Black and White Image")
plt.figure()
plt.imshow(bw_image_restored, cmap="gray")
plt.title("Restored Black and White Image")

plt.figure()
plt.imshow(color_image)
plt.title("Original Color Image")
plt.figure()
plt.imshow(color_image_restored)
plt.title("Restored Color Image")

plt.show()