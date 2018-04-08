from os.path import join

from solid.utils import *

NAME = "esp32"


class ESP32:
    base = {
        "l": 51.6,
        "w": 28.5,
        "h": 1.6
    }

    hole_d = 3.05

    def __init__(self):
        pass

    def _generate_holes(self):
        _ = []
        h = forward(self.hole_d / 2)(right(self.hole_d / 2)(hole()(cylinder(d=self.hole_d, h=self.base["h"]))))
        _.append(right(0.95)(forward(0.9)(h)))
        _.append(right(0.95)(forward(self.base["w"] - self.hole_d - 1)(h)))
        _.append(right())
        return _

    def assemble(self):
        o = cube([self.base["l"], self.base["w"], self.base["h"]])
        o += self._generate_holes()
        return o


if __name__ == '__main__':
    scad_render_to_file(ESP32().assemble(), join('./out/', NAME + ".scad"), file_header='$fn = 42;')
