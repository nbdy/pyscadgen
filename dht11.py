from os.path import join

from solid.utils import *

from pin import Pin

SEGMENTS = 42
NAME = "dht11"


class DHT11:
    length = 16
    width = 12.5
    height = 5.75

    def __init__(self):
        pass

    def assemble(self):
        base = cube([self.length, self.width, self.height])
        p = Pin(pin_length=7.5)
        for i in range(1, 5):
            base += forward(2.8 * i - 2.05 / 2)(rotate([0, 270, 0])(right(2.8)(cylinder(d=0.5, h=7.5))))
        return base


if __name__ == '__main__':
    scad_render_to_file(DHT11().assemble(), join('./out/', NAME + ".scad"), file_header='$fn = %s;' % SEGMENTS)
