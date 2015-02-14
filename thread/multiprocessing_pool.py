#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 15-2-15
__author__ = 'cluo'
import os
import PIL

from multiprocessing import Pool
from PIL import Image

SIZE = (75, 75)
SAVE_DIRECTORY = 'thumbs'

def get_image_paths(folder):
    return (os.path.join(folder, f)
            for f in os.listdir(folder)
            if 'jpg' in f)

def create_thumbnail(filename):
    im = Image.open(filename)
    im.thumbnail(SIZE, Image.ANTIALIAS)
    base, fname = os.path.split(filename)
    save_path = os.path.join(base, SAVE_DIRECTORY, fname)
    im.save(save_path)

if __name__ == '__main__':
    folder = os.path.abspath('./img')
    thumb_path = os.path.join(folder, SAVE_DIRECTORY)
    if os.path.exists(thumb_path) == False:
        os.mkdir(thumb_path)
    images = get_image_paths(folder)
    pool = Pool()
    pool.map(create_thumbnail, images)
    pool.close()
    pool.join()


