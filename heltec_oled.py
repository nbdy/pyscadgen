from os.path import join

from solid.utils import *

SEGMENTS = 42
HAS_PINS = True
PINS_BACKSIDE = False


def assemble():
    print "assembling"
    base = cube([27.2, 27, 1])

    print "punching holes"
    _cylinder_hole = down(20)(hole()())
    base += forward(3)(right(2)(_cylinder_hole))

    return base


if __name__ == '__main__':
    scad_render_to_file(assemble(), join('./out/', "heltec_oled.scad"), file_header='$fn = %s;' % SEGMENTS)
