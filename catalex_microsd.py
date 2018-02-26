from os.path import join

from solid.utils import *

SEGMENTS = 42
NAME = "catalex_microsd"
HAS_PINS = True
PINS_BACKSIDE = False


# basically the same as the AZDelivery SD module
class CatalexMicroSD:
    length = 41.5
    width = 23.5
    height = 1.1

    def __init__(self, has_pins=True, pins_bent=True):
        self._has_pins = has_pins
        self._pins_bent = pins_bent

    def assemble(self):
        base = cube([self.length, self.width, self.height])

        _cylinder_hole = down(20)(hole()(cylinder(d=2, h=50)))
        base += right(2)(forward(1.5)(_cylinder_hole))
        base += right(2)(forward(21.5)(_cylinder_hole))
        base += right(39.5)(forward(1.5)(_cylinder_hole))
        base += right(39.5)(forward(21.5)(_cylinder_hole))

        _cube_chip1 = forward(3)(right(12)(up(1.1)(cube([4, 5, 1]))))
        _cube_chip2 = forward(14.5)(right(10.9)(up(1.1)(cube([6.2, 3.5, 1.6]))))
        base += _cube_chip1
        base += _cube_chip2

        _cube_slot = cube([14.5, 14.7, 1.9])
        base += up(1.1)(forward(4.3)(right(25.5)(_cube_slot)))

        if HAS_PINS:
            _cube_pins = cube([2.5, 15, 2.5])
            if PINS_BACKSIDE:
                _cube_pins = down(2.5)(_cube_pins)
            else:
                _cube_pins = up(1.1)(_cube_pins)
            base += forward(4)(right(2.5)(_cube_pins))

        return base


if __name__ == '__main__':
    scad_render_to_file(CatalexMicroSD().assemble(), join('./out/', NAME + ".scad"), file_header='$fn = %s;' % SEGMENTS)
