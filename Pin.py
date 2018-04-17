from os.path import join

from solid.utils import *

SEGMENTS = 42
NAME = "pin"


# todo angle
# todo solder top
class Pin:
    base_width = 2.54
    base = cube([base_width, base_width, base_width])

    def __init__(self, bent=False, solder_hat=True, segments=42, angle=90, pin_length=6, pin_diameter=1,
                 pcb_height=1.6):
        self.pcb_height = pcb_height
        self.bent = bent
        self.solder_hat = solder_hat
        self.segments = segments
        self.angle = angle
        self.pin_length = pin_length
        self.pin_diameter = pin_diameter

    def assemble(self):
        pin = cylinder(h=self.pin_length, d=self.pin_diameter)
        if self.solder_hat:
            solder_hat = cylinder(h=1, d1=1.9, d2=0.6)
            self.base += right(self.base_width / 2)(forward(self.base_width / 2)(up(self.pcb_height + self.base_width)(
                solder_hat)))
        if self.bent:
            self.base += right(self.base_width / 2)(
                forward(self.base_width / 2)(up(self.base_width / 2 - self.pin_length)(
                    rotate_extrude(10)(circle(d=self.base_width))))
            )
        else:
            self.base += right(self.base_width / 2)(forward(self.base_width / 2)(
                up(self.base_width / 2 - self.pin_length)(pin)))
        return self.base


if __name__ == '__main__':
    scad_render_to_file(Pin().assemble(), join('./out/', NAME + ".scad"), file_header='$fn = %s;' % SEGMENTS)
