from os.path import join

from solid.utils import *

SEGMENTS = 42
NAME = "sd_card.scad"


class SDCard:
    width = 23.8
    length = 31.8
    height = 2.1

    def __init__(self, extra=0):
        self.width += extra
        self.length += extra
        self.height += extra

    def assemble(self):
        return cube([self.width, self.length, self.height])


if __name__ == '__main__':
    sd_card = SDCard()
    scad_render_to_file(sd_card.assemble(), join('./out/', NAME), file_header='$fn = %s;' % SEGMENTS)
