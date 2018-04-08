from os.path import join

from solid.utils import *

NAME = "spoon_end"


def assemble():
    o = forward(12.2 / 2 - 1.5)(cube([12.2, 3.1, 9.3]))
    o += right(3)(cube([6, 12.2, 9.3]))
    o += forward(12.2 / 2)(right(6)(up(9.3)(cylinder(d=12.2, h=20))))
    o += forward(12.2 / 2)(right(6)(up(9.3 + 20)(sphere(d=12.2))))
    o += forward(12.2 / 2)(up(9.3 + 12)(left(5)(rotate([0, 90, 0])(hole()(cylinder(d=8, h=20))))))
    return o


if __name__ == '__main__':
    scad_render_to_file(assemble(), join('./out/', NAME + ".scad"), file_header='$fn = 42;')
