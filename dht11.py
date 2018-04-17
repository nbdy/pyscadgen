from os.path import join
from solid.utils import *

from Case import Case
from Pin import Pin

NAME = "dht11"


class DHT11:
    length = 16
    width = 12.5
    height = 5.75

    def __init__(self):
        pass

    def assemble(self):
        base = cube([self.length, self.width, self.height])
        p = Pin(True, pin_length=7.5)
        for i in range(0, 4):
            base += forward(i * p.base_width)(forward(1)(
                up(self.height / 2 + p.base_width / 2)(rotate([0, 90, 0])(p.assemble()))))
        return base


# todo air slots / pins
class DHT11Case(Case):
    positive = DHT11


if __name__ == '__main__':
    scad_render_to_file(DHT11().assemble(), join('./out/', NAME + ".scad"), file_header='$fn = 42;')
    scad_render_to_file(DHT11Case().bottom(), join('./out/', NAME + "_bottom.scad"), file_header='$fn = 42;')
    scad_render_to_file(DHT11Case().top(), join('./out/', NAME + "_top.scad"), file_header='$fn = 42;')
