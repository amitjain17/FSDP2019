# -*- coding: utf-8 -*-
"""
Created on Sat May 18 12:53:21 2019

@author: NITS
"""

from PIL import Image
img = Image.open("b.jpg")
img1 = img.transpose(Image.ROTATE_90)