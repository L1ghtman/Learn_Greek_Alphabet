import pygame as pg
import os
import sys
import random

from letter_images import *
from settings import *

class Level:
    def __init__(self, buttons):
        pg.init()

