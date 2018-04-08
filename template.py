from os.path import join

from solid.utils import *

NAME = ""


def assemble():
    return


if __name__ == '__main__':
    scad_render_to_file(assemble(), join('./out/', NAME + ".scad"), file_header='$fn = 42;')
