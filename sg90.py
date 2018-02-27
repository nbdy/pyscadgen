from os.path import join

from solid.utils import *

SEGMENTS = 42
NAME = "sg90"


class SG90:
    length = 22.5
    width = 12.5
    height = 22.2

    holder_length = 32.2
    holder_height = 2.5
    holder_hole_diameter = 2.2

    holder_offset = {
        "up": 18.1 - holder_height,
        "left": 4.5
    }

    top_thingy_height = 26.5 - height

    def __init__(self):
        pass

    def assemble(self):
        base = cube([self.length, self.width, self.height])
        base += left(self.holder_offset["left"])(up(self.holder_offset["up"])(
            cube([self.holder_length, self.width, self.holder_height])))
        h = forward(5 + self.holder_hole_diameter / 2)(hole()(cylinder(d=self.holder_hole_diameter, h=50)))
        base += left(1 + self.holder_hole_diameter / 2)(h)
        base += right(1 + self.holder_hole_diameter / 2 + self.length)(h)
        base += forward(self.width / 2)(
            up(self.height)(right(self.width / 2)(cylinder(d=self.width, h=(26.9 - self.height)))))
        base += forward(self.width / 2)(up(self.height)(right(self.width)(cylinder(d=5.5, h=(26.9 - self.height)))))
        base += forward(self.width / 2)(up(26.9)(right(self.width / 2)(cylinder(h=(28.75 - 26.9), d=4.85))))
        return base


if __name__ == '__main__':
    scad_render_to_file(SG90().assemble(), join('./out/', NAME + ".scad"), file_header='$fn = %s;' % SEGMENTS)
