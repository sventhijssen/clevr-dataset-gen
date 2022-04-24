import os
import numpy as np

from PIL import Image

path = os.path.expanduser('~') + "/Documents/ucf/2022-spring/cap6121/clevr-dataset-gen/clevr-dataset-gen/dataset/color_shapes/images"


for filename in os.listdir(path):

    filepath = path + os.sep + filename

    if "mask" in filename:
        img = Image.open(filepath)
        data = np.array(img)

        r1, g1, b1 = 0, 0, 0  # Original value
        r2, g2, b2 = 64, 64, 64  # Value that we want to replace it with

        red, green, blue = data[:, :, 0], data[:, :, 1], data[:, :, 2]
        mask = (red == r1) & (green == g1) & (blue == b1)
        data[:, :, :3][mask] = [r2, g2, b2]

        im = Image.fromarray(data)
        im.save(filepath)
