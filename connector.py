from os.path import join

from solid.utils import *

SEGMENTS = 42
NAME = "connector"


class ClickConnector:
    x_connector_angle = 45

    def __init__(self, length=20, height=3, width=10, thickness=3, ):
        self.length = length
        self.width = width
        self.height = height
        self.thickness = thickness
        self.base = cube([length, width, height])
        self.connector = cube([length, width, height / 2]) + up(height / 2)(cube([length / 8, width, height / 2]))

    def generate_lock(self):
        b = up(self.height * 0.5)(forward(self.width)(right(self.length - self.thickness / 2)(sphere(d=self.height))))
        return b

    def generate_hook_pin_holder(self):
        b = right(self.length - self.thickness)(forward(self.width + self.thickness)(
            cube([self.thickness, self.thickness, self.height])))
        b += hole()(right(self.length - self.thickness / 2)(
            forward(self.width + self.thickness + self.thickness / 2)(cylinder(d=self.thickness / 2, h=self.height))))
        return b

    def hook(self):
        b = cube([self.length, self.thickness, self.height])
        b += up(self.height)(cube([self.length, self.width + self.thickness, self.height / 2]))
        b += hole()(forward(self.thickness)(up(self.height)(cube([self.length, self.width, 0.5]))))  # split top / hook
        b += cube([self.thickness, self.width, self.height])
        b += forward(self.width)(cube([self.length, self.thickness, self.height]))
        b += self.generate_lock()
        b += self.generate_hook_pin_holder()
        return b

    def bottom(self):
        b = down(self.height)(cube([self.length, self.width, self.height * 2]))
        b += hole()(self.hook())
        return b


if __name__ == '__main__':
    scad_render_to_file(ClickConnector().hook(), join('./out/', NAME + ".scad"),
                        file_header='$fn = %s;' % SEGMENTS)
