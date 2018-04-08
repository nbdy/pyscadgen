from os.path import join
from solid.utils import *

SEGMENTS = 42
NAME = "RoundChipConnector"


class RoundChipConnector:
    length = 5
    width = 2
    height = 10

    def __init__(self, length=5, width=2, height=10):
        self.base = up(height / 2)(cube([length, width, height], center=True))
        self.length = length
        self.width = width
        self.height = height
        pass

    def assemble(self):
        o = [up(self.width / 2 + 1)(sphere(d=self.width + 1)), up(self.height - self.width)(sphere(d=self.width + 1))]
        return self.base + o


if __name__ == '__main__':
    scad_render_to_file(RoundChipConnector().assemble(), join('./out/', NAME + ".scad"),
                        file_header='$fn = %s;' % SEGMENTS)
