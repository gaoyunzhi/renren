# -*- coding: utf8 -*-
import re

INPUT_DIR = r'C:\Users\gyz\Pictures'
ALBUM_DIR = '../..'

ALBUM_FILE = re.compile(r'^.* - .* - (.*).htm$')
PHOTO_REG = re.compile(r'<img alt="((.*\n){0,7}.*)" class="loading" data-src="(.*)" src')