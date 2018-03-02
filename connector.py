from os.path import join

from solid.utils import *

SEGMENTS = 42
NAME = "connector"


class SlideConnector:
    x_connector_angle = 45

    def __init__(self, length=20, height=3, width=10, thickness=3):
        self.length = length
        self.width = width
        self.height = height
        self.thickness = thickness
        self.base = cube([length, width, height])
        self.connector = cube([length, width, height / 2]) + \
                         up(height / 2)(cube([length / 8, width, height / 2]))

    def generate_pin(self):
        b = forward(self.width - self.thickness)(
            right(self.length / 2)(up(self.height / 2)(sphere(d=self.thickness / 4))))
        return b

    def bottom(self):
        b = cube([self.length, self.thickness, self.height])
        b += cube([self.thickness, self.width, self.height])
        b += forward(self.width)(cube([self.length / 2, self.thickness, self.height]))
        b += self.generate_pin()
        return b

    def top(self):
        return


if __name__ == '__main__':
    scad_render_to_file(SlideConnector().generate_pin(), join('./out/', NAME + ".scad"),
                        file_header='$fn = %s;' % SEGMENTS)
