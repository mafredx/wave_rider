"""
Wave Rider -- global_variables.py

    Module to load game resources from Resources directory.

Author: Mike Fredricks
Genesis: 2/13/22
"""
import os
import random
from waverider.Module import global_variables as gv
import pygame as pg

# Function made to load an image from Resources and return image object
def load_image(name, colorkey=None, scale=1):
    fullname = os.path.join(gv.resource_directory, name)

    try:
        image = pg.image.load(fullname)
        if image.get_alpha() is None:

            # Scale image
            if scale != 1:
                size = image.get_size()
                size = (size[0] * scale, size[1] * scale)
                image = pg.transform.scale(image, size)

            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame.error:
        raise SystemError("Cannot load image: " + fullname)

    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pg.RLEACCEL)

    return image, image.get_rect()

# Function made to load a sound from Resources
def load_sound(name):
    class NoneSound:
        def play(self):
            pass

    # Dummy sound returned if mixer class doesn't work
    if not pg.mixer or not pg.mixer.get_init():
        return NoneSound()

    fullname = os.path.join(data_dir, name)

    try:
        sound = pg.mixer.Sound(fullname)
    except pygame.error:
        raise SystemError("Cannot load sound: " + fullname)

    return sound

# Function made to choose random file from a folder
def random_file(folder):
    file = random.choice(folder)
    return file















