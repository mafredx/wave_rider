"""
Wave Rider -- interactive_objects.py

    Script containing interactive object classes. This includes the wave rider character, game world,
    tokens, and all other interactive objects.

Author: Mike Fredricks
Genesis: 2/13/22
"""

import pygame as pg
from waverider.Module import load_resources as lr
import math

# Class made to handle all behaviors of the game's player character, wave rider
class Rider(pg.sprite.Sprite):
    """
    Returns: rider object
    Methods: update, render, amplitude_control
    Attributes: area
    """
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image, self.rect = lr.load_image("Rider.png")
        screen = pg.display.get_surface()
        self.area = screen.get_rect()
        self.rect.center = self.area.right/4 , self.area.bottom/2
        self.amplitude = 100
        self.wavelength = 100
        self.velocity =
        self.state = 'sine'

    def update(self):
        if self.state == 'sine' and self.rect.centery < self.amplitude:


        #new_position = self.get_new_position(self.rect, self.y_speed)
        #self.rect = new_position

    # Function to return position of sinusoidal motion
    def sine_motion(self, time):
        y_pos = self.amplitude * math.sin(2*math.pi*self.frequency*time/1000)


    # User input control method for amplitude of wave rider's wave
    def amplitude_control(self):
        pass

    # User input control methods for frequency of wave rider's wave
    def frequency_control(self):
        pass

# Class made to handle the blips (lil sound bytes that the player scores points from)
class Blip(pg.sprite.Sprite):
    """
    Returns: blip object
    Methods: update, hover, make_sound, add_score
    Attributes: points, hover_frequency
    """
    def __init__(self, points, hover_frequency):
        pg.sprite.Sprite.__init__(self)
        self.score_value = points
        self.hover_frequency = hover_frequency

    #TODO: figure out what is needed for this class object's update method
    def update(self):
        pass

    # Method to make token hover slightly up and down on the screen
    def hover(self):
        pass

    # Method to make a sound when the player comes in contact with a blip
    def make_sound(self, sound_file, random=False):
        if random:
            blip_sounds_folder = os.path.join("Resources", "blip_sounds")
            lr.load_sound(lr.random_file(blip_sounds_folder))
        else:
            lr.load_sound(sound_file)

    # Method to add blip score value to player's game scoreboard (TODO: fill this in)
    def add_score(self):
        pass

















