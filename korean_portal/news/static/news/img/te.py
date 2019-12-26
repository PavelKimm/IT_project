import os, sys
from PIL import Image

size = 500, 500



im = Image.open('test.png')
im.thumbnail(size, Image.ANTIALIAS)
im.save('test.png', "png")
