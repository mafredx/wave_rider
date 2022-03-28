"""
Wave Rider -- display_objects.py

    Script containing display object classes. This includes the background, scoreboard, and all other non-interactive
    display objects.

Author: Mike Fredricks
Genesis: 3/6/22
"""

import pygame as pg
from Module import load_resources as lr
import math


# Class made to handle the game's scrolling background in which wave rider lives and moves about
class Background:
    """
    Returns: background object
    Methods: update, render, get_new_scroll_speed
    Attributes: scroll_speed
    """
    def __init__(self):
        self.bg_image = lr.load_image('Wave_Land_1')        #TODO: create background image named 'Wave_Land_1'
        self.bg_rect = self.bg_image.get_rect()

        self.bg_x1 = 0
        self.bg_y1 = 0

        self.bg_x2 = self.bg_rect.width
        self.bg_y2 = 0

        self.initial_scroll_speed = 5
        self.scroll_speed = self.initial_scroll_speed       #TODO: figure out relative speed values

    # Method to reset background variables to original states
    def re_init(self):
        self.scroll_speed = self.initial_scroll_speed

    def update(self):
        self.bg_x1 -= self.scroll_speed
        self.bg_x2 -= self.scroll_speed
        if self.bg_x1 <= -self.bg_rect.width:
            self.bg_x1 = self.bg_rect.width
        if self.bg_x2 <= -self.bg_rect.width:
            self.bg_x2 = self.bg_rect.width

    def render(self):
        screen = pg.display.get_surface()
        screen.blit(self.bg_image, (self.bg_x1, self.bg_y1))
        screen.blit(self.bg_image, (self.bg_x2, self.bg_y2))

    # Method to get a new scroll speed if needed (i.e. player gains a boost)
    def get_new_scroll_speed(self, scaler):
        new_scroll_speed = self.scroll_speed * scaler
        return new_scroll_speed


# Class made to handle the player scoreboard
class ScoreBoard:
    """
    Returns: scoreboard object
    Methods: display, update, flash
    Attributes: score
    """
    def __init__(self, score):
        self.score = score

    # TODO: fill this function in
    def display(self):
        pass

    # TODO: fill this function in
    def update(self):
        pass















