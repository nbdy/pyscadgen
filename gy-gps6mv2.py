from os.path import join

from solid.utils import *

from pin import Pin

SEGMENTS = 42
NAME = "gy-gps6mv2"
HAS_PINS = False
PINS_BACKSIDE = True
HAS_ANTENNA = True
ANTENNA_ANGLE = 90


class gyGPS6mv2:
    length = 35.5
    width = 26.4
    height = 1.1

    def __init__(self, has_pins=True, pins_bent=False, pins_backside=True, has_antenna=True):
        self._has_antenna = has_antenna
        self._has_pins = has_pins
        self._pins_bent = pins_bent
        self._pins_backside = pins_backside

    def assemble(self):
        base = cube([self.length, self.width, self.height])

        _hole_cylinder = hole()(down(20)(cylinder(d=3, h=50)))
        base += right(2.5)(forward(3)(_hole_cylinder))
        base += right(2.5)(forward(23.5)(_hole_cylinder))
        base += right(33)(forward(3)(_hole_cylinder))
        base += right(33)(forward(23.5)(_hole_cylinder))

        _big_hole = hole()(down(20)(cylinder(d=4, h=50)))
        base += right(3)(forward(12.7)(_big_hole))

        base += right(9.7)(forward(5.7)(cube([12.1, 16, 2.3])))

        base += right(2.5)(forward(7.5)(cylinder(d=1.5, h=1.2)))

        if self._has_pins:
            p = Pin(self._pins_bent)
            for i in range(0, 3):
                if self._pins_backside:
                    base += right(self.length - p._base_width)(
                        down(p._base_width)(forward(8.6 + i * p._base_width)(p.assemble())))
                else:
                    base += right(self.length - p._base_width)(
                        up(self.height)(forward(8.6 + i * p._base_width)(p.assemble())))
        else:
            _pin_hole = right(33.3)(hole()(cylinder(d=0.5, h=50)))
            base += forward(8.6)(_pin_hole)
            base += forward(11.45)(_pin_hole)
            base += forward(14.15)(_pin_hole)
            base += forward(16.6)(_pin_hole)

        if HAS_ANTENNA:
            _antenna = cube([25.1, 25.3, 8.5])
            _antenna_cable = rotate([0, 270, 0])(cylinder(d=1, h=22))
            _antenna += up(2.2)(forward(12)(_antenna_cable))
            base += rotate([0, 0, ANTENNA_ANGLE * 2])(right(19.5)(back(19.5)(_antenna)))

        return base


if __name__ == '__main__':
    scad_render_to_file(gyGPS6mv2().assemble(), join('./out/', NAME + ".scad"), file_header='$fn = %s;' % SEGMENTS)
