from os.path import join

from solid.utils import *

SEGMENTS = 42
NAME = "pin"


# todo angle
# todo solder top
class Pin:
    base_width = 2.5
    base = cube([base_width, base_width, base_width])

    def __init__(self, bent=False, segments=42, angle=90, pin_length=6, pin_diameter=0.6):
        self.bent = bent
        self.segments = segments
        self.angle = angle
        self.pin_length = pin_length
        self.pin_diameter = pin_diameter

    def assemble(self):
        pin = cylinder(h=self.pin_length, d=self.pin_diameter)
        if self.bent:
            self.base += right(self.base_width / 2)(
                forward(self.base_width / 2)(up(self.base_width / 2 - self.pin_length)(
                    rotate_extrude(10)(circle(d=self.base_width))))
            )
        else:
            self.base += right(self.base_width / 2)(
                forward(self.base_width / 2)(up(self.base_width / 2 - self.pin_length)(pin)))
        return self.base


if __name__ == '__main__':
    scad_render_to_file(Pin(True).assemble(), join('./out/', NAME + ".scad"), file_header='$fn = %s;' % SEGMENTS)
