from os.path import join

from solid.utils import *

SEGMENTS = 42
NAME = "pin"


# todo angle
class Pin:
    _base_width = 2.5
    _pin_length = 6
    _pin_width = 0.6

    base = cube([_base_width, _base_width, _base_width])
    pin = cylinder(h=_pin_length, d=_pin_width)

    def __init__(self, bent=False, segments=42, angle=90, pin_length=6):
        self.bent = bent
        self.segments = segments
        self.angle = angle
        self._pin_length = pin_length

    def assemble(self):
        if self.bent:
            pass
        else:
            self.base += right(self._base_width / 2)(
                forward(self._base_width / 2)(up(self._base_width / 2 - self._pin_length)(self.pin)))
        return self.base


if __name__ == '__main__':
    scad_render_to_file(Pin().assemble(), join('./out/', NAME + ".scad"), file_header='$fn = %s;' % SEGMENTS)
