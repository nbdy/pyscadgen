$fn = 42;

cube(size = [23.8000000000, 31.8000000000, 2.1000000000]);
/***********************************************
*********      SolidPython code:      **********
************************************************
 
from os.path import join
from solid.utils import *

SEGMENTS = 42
NAME = "sd_card.scad"


class SDCard:
    width = 23.8
    length = 31.8
    height = 2.1

    def __init__(self):
        pass

    def assemble(self):
        return cube([self.width, self.length, self.height])


if __name__ == '__main__':
    sd_card = SDCard()
    scad_render_to_file(sd_card.assemble(), join('./out/', NAME), file_header='$fn = %s;' % SEGMENTS)
 
 
************************************************/
