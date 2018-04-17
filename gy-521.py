from os.path import join
from solid.utils import *

from Pin import Pin

SEGMENTS = 42
NAME = "gy-521"


class GY521:
    length = 20.8
    width = 15.7
    height = 1.2

    onboard_cube = {
        "length": 16.8,
        "width": 5.8,
        "height": 2.35 - height
    }

    bigger_chip = {
        "length": 3.3,
        "width": 1.7,
        "height": 3 - height,
        "forward": 3.65 - 1.7,
        "right": length - 12
    }

    hole_diameter = 3.2

    def __init__(self):
        pass

    def assemble(self):
        b = cube([self.length, self.width, self.height])
        b += right(self.length - self.onboard_cube["length"])(forward(4.35)(up(self.height)(
            cube([self.onboard_cube["length"], self.onboard_cube["width"], self.onboard_cube["height"]]))))
        b += forward(self.bigger_chip["forward"])(right(self.bigger_chip["right"])(
            cube([self.bigger_chip["length"], self.bigger_chip["width"], self.bigger_chip["height"]])))

        h = hole()(forward(1 + self.hole_diameter / 2)(cylinder(d=self.hole_diameter, h=self.height)))
        b += right(1.25 + self.hole_diameter / 2)(h)
        b += right(16.6 + self.hole_diameter / 2)(h)

        p = down(Pin.base_width)(forward(self.width - Pin.base_width)(Pin().assemble()))
        for i in range(0, 8):
            b += right(Pin.base_width * i + 0.4)(p)
        return b


if __name__ == '__main__':
    scad_render_to_file(GY521().assemble(), join('./out/', NAME + ".scad"), file_header='$fn = %s;' % SEGMENTS)
