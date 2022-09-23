import os
import numpy as np
from PIL import Image,ImageDraw
import matplotlib.pyplot as plt

jpg = './JPEGImages/'
png = './SegmentationClass/'

for j,p in zip(os.listdir(jpg)[10:],os.listdir(png)[10:]):
    j = jpg+j
    p = png + p
    image1 = Image.open(j)
    image2 = Image.open(p)
    image2 = np.array(image2)*255.
    image2 = Image.fromarray(image2)
    image1.show()
    image2.show()
    # plt.imshow(image2)
    # plt.axis('off')
    # plt.show()
    break
