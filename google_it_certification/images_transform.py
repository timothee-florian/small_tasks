#!/usr/bin/env python3

import os
from PIL import Image

def transform_image(image_name, new_size, rotation=0, format = 'jpg', folder = 'new_images'):
    """
    Will load the image resize, rotate and save it in the given format.
    """
    im = Image.open(image_name)
    if im.mode != 'RGB':
        im = im.convert('RGB')
    new_im = im.resize(new_size)
    new_im = new_im.rotate(rotation)
    new_name = '.'.join(image_name.split('.')[:])
    new_im.save(os.path.join(folder, new_name), format)



folder_path = 'images'
home_path = os.path.expanduser("~")
folder_path = os.path.join(home_path, folder_path)


images = os.listdir(folder_path)
os.chdir(folder_path)

for image in images:
    if not os.path.isfile(image) or image[:2] != 'ic':
        continue
    transform_image(image, new_size= (128, 128), rotation=-90, format = 'jpeg')
