from os.path import join

from solid.utils import *

SEGMENTS = 42
NAME = ""


def assemble():
    return


if __name__ == '__main__':
    scad_render_to_file(assemble(), join('./out/', NAME + ".scad"), file_header='$fn = %s;' % SEGMENTS)
