from os.path import join

from solid.utils import *

NAME = "DoubleHalfAnkerConnector"


class DoubleHalfAnkerConnector:
    def __init__(self, length=10, width=2, ankerWidth=3, ankerLength=4, distanceBetween=4):
        self.ankerWidth = ankerWidth
        self.distanceBetween = distanceBetween
        self.ankerLength = ankerLength
        self.width = width
        self.length = length
        self.base = cube([width, width, length])
        self.halfAnker = cube([ankerWidth, width, ankerLength]) + rotate([0, 45, 0])(left(ankerWidth)(hole()(
            cube([ankerWidth, width + 1, ankerLength]))))

    def assemble(self):
        return self.base + [right(self.distanceBetween)(self.base), left(self.width)(self.halfAnker),
                            right(self.width + self.ankerWidth * 2)(forward(self.width)(rotate([0, 0, 180])(
                                self.halfAnker))), up(self.length)(
                cube([self.distanceBetween + self.width, self.width, self.width])), up(self.ankerLength + self.width)(
                left(self.width)(cube([self.width, self.width, self.width]))),
                            right(self.width + self.distanceBetween)(
                                up(self.ankerLength + self.width)(cube([self.width, self.width, self.width])))]


if __name__ == '__main__':
    scad_render_to_file(DoubleHalfAnkerConnector().assemble(), join('./out/', NAME + ".scad"), file_header='$fn = 42;')
