from os.path import join

from solid.utils import *

SEGMENTS = 42
NAME = "pin"


class Pin:
    _base_width = 2.5
    _pin_length = 6
    _pin_width = 0.6

    base = cube([_base_width, _base_width, _base_width])
    pin = cylinder(h=_pin_length, d=_pin_width)

    def __init__(self, bent=True, segments=42):
        self.bent = bent
        self.segments = segments

    def assemble(self):
        if self.bent:
            for i in range(self.segments):
                a = i * 90 / self.segments
        else:
            self.base += right(self._base_width / 2)(
                forward(self._base_width / 2)(up(self._base_width / 2 - self._pin_length)(self.pin)))
        return self.base


if __name__ == '__main__':
    scad_render_to_file(Pin().assemble(), join('./out/', NAME + ".scad"), file_header='$fn = %s;' % SEGMENTS)
