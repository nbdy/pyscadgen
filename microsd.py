from os.path import join

from solid.utils import *

SEGMENTS = 42
NAME = "microsd"


class MicroSD:
    length = 15
    width = 10.95
    height = 1

    def __init__(self):
        pass

    def assemble(self):
        # todo round corners
        base = cube([self.length, self.width, self.height])
        base += down(1)(forward(10.3)(right(5.65)()(hole()(cube([1.5, 1.5, 3])))))
        base += down(1)(forward(9.65)(right(9.9)(hole()(cube([10, 1.5, 3])))))
        return base


if __name__ == '__main__':
    scad_render_to_file(MicroSD().assemble(), join('./out/', NAME + ".scad"), file_header='$fn = %s;' % SEGMENTS)
