from os.path import join
from solid.utils import *

from Pin import Pin

SEGMENTS = 42
NAME = "sim800l"


class Sim800L:
    length = 21.6
    width = 17.6
    height = 1.25

    _chip_length = 17
    _chip_width = 15.45
    _chip_height = 3.5 - height

    _sd_holder_height = 2.6
    _sd_holder_length = 15.6
    _sd_holder_width = 15.3

    def __init__(self, has_pins=True, pins_backside=True):
        self._has_pins = has_pins
        self._pins_backside = pins_backside

    def assemble(self):
        base = cube([self.length, self.width, self.height])
        chip = cube([self._chip_length, self._chip_width, self._chip_height])
        base += up(self.height)(right(21 - self._chip_length)(forward(17 - self._chip_width)(chip)))
        base += down(self._sd_holder_height)(right(21.4 - self._sd_holder_length)(
            cube([self._sd_holder_length, self._sd_holder_width, self._sd_holder_height])))
        if self._has_pins:
            p = Pin()
            for i in range(1, 6):
                base += forward((4.5 - p._base_width) + i * p._base_width)(down(p._base_width)(p.assemble()))
        return base


if __name__ == '__main__':
    scad_render_to_file(Sim800L().assemble(), join('./out/', NAME + ".scad"), file_header='$fn = %s;' % SEGMENTS)
