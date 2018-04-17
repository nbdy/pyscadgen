from os.path import join
from solid.utils import *

from Pin import Pin

SEGMENTS = 42
NAME = "max4466"


class Max4466:
    length = 21.5
    width = 14
    height = 1.6

    _microphone_diameter = 9.6
    _microphone_height = 7.2

    has_pins = True

    _hole_diameter = 2.6

    _potentiometer_height = 1.2
    _potentiometer_diameter = 3.2

    def __init__(self, pins_bent=True):
        self.pins_bent = pins_bent

    def assemble(self):
        base = cube([self.length, self.width, self.height])
        h = down(20)(hole()(cylinder(d=self._hole_diameter, h=100)))
        base += forward(1.15 + self._hole_diameter / 2)(right(1.15 + self._hole_diameter / 2)(h))
        base += forward(10.55 + self._hole_diameter / 2)(right(1.15 + self._hole_diameter / 2)(h))
        m = up(self.height)(cylinder(h=self._microphone_height, d=self._microphone_diameter))
        base += forward(11.65 - self._microphone_diameter / 2)(right(12.25 - self._microphone_diameter / 2)(m))
        r = down(2.18 - self.height)(cube([12.80, 13, 2.18 - self.height]))
        base += forward(0.5)(right(5)(r))
        p = cylinder(d=self._potentiometer_diameter, h=self._potentiometer_height)
        base += down(self.height - self._potentiometer_height)(right(17.65 - self._potentiometer_diameter / 2)(
            forward(10.95 - self._potentiometer_diameter / 2)(p)))
        for i in range(0, 3):
            p = Pin(self.pins_bent)
            base += forward(3.3 + i * p._base_width)(down(p._base_width)(right(21.6 - p._base_width)(p.assemble())))
        return base


if __name__ == '__main__':
    scad_render_to_file(Max4466(False).assemble(), join('./out/', NAME + ".scad"), file_header='$fn = %s;' % SEGMENTS)
