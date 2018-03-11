from os.path import join

from solid.utils import *

SEGMENTS = 42
NAME = "pinConnector"


class PinConnector:
    def __init__(self, base_height=2, base_diameter=5, pin_diameter=2, pin_length=10, hook_width=3, hook_type="cone"):
        self.base_height = base_height
        self.pin_diameter = pin_diameter
        self.pin_length = pin_length
        self.base_diameter = base_diameter
        self.hook_width = hook_width
        self.hook_type = hook_type

    def bottom(self):
        b = cylinder(h=self.base_height, d=self.base_diameter)
        b += up(self.base_height)(cylinder(h=self.pin_length, d=self.pin_diameter))
        b = self.generate_hook(b)
        return b

    def generate_hook(self, b):
        if self.hook_type == "cone":
            b += self.generate_cone_hook()

        return b

    def generate_cone_hook(self):
        cone = cylinder(d1=self.pin_diameter, d2=0, h=self.pin_diameter)
        r = up(self.pin_length + self.base_height / 2)(rotate([0, 90, 0])(cone))
        r += up(self.pin_length + self.base_height / 2)(rotate([0, 270, 0])(cone))
        return r

    def top(self):
        b = cylinder(h=self.base_height + self.pin_length, d=self.base_height)
        b += hole()(self.assemble())


if __name__ == '__main__':
    scad_render_to_file(PinConnector().assemble(), join('./out/', NAME + ".scad"), file_header='$fn = %s;' % SEGMENTS)
