from os.path import join
from solid.utils import *


class RPiZeroCase:
    name = "RPiZeroCase"

    width = 30.25
    length = 65
    height = 1.5

    def __init__(self, extra=0):
        self.width += extra
        self.length += extra
        self.height += extra

    def assemble(self):
        return cube([self.width, self.length, self.height])


class RaspwnCase:
    name = "RaspwnCase"

    wall_thickness = 1
    length = 64.95
    width = 30.3
    height = 5

    def __init__(self, wall_thickness=1):
        self.wall_thickness = wall_thickness

    def bottom(self):
        lw = self.length + self.wall_thickness * 2
        ww = self.width + self.wall_thickness * 2
        a = [cube([lw, self.wall_thickness, 5]),
             cube([self.wall_thickness, ww, 5]),
             right(lw - self.wall_thickness)(cube([self.wall_thickness, ww, 5])),
             forward(ww - self.wall_thickness)(cube([lw, self.wall_thickness, 5])),
             forward(3.65 + self.wall_thickness)(
                 right(3.5 + self.wall_thickness)(up(self.wall_thickness)(cylinder(r=3.125, h=1.25)))),
             # podest cylinder
             forward(ww - 6 + self.wall_thickness)(
                 right(3.5 + self.wall_thickness)(up(self.wall_thickness)(cylinder(r=3.125, h=1.25)))),
             forward(3.65 + self.wall_thickness)(
                 right(self.length + self.wall_thickness - 3.55)(up(self.wall_thickness)(cylinder(r=3.125, h=1.25)))),
             forward(ww - 6 + self.wall_thickness)(
                 right(self.length + self.wall_thickness - 3.55)(up(self.wall_thickness)(cylinder(r=3.125, h=1.25)))),
             forward(3.65 + self.wall_thickness)(
                 right(3.5 + self.wall_thickness)(up(self.wall_thickness + 1.25)(cylinder(r=1, h=1.5)))),  # hole
             forward(ww - 6 + self.wall_thickness)(
                 right(3.5 + self.wall_thickness)(up(self.wall_thickness + 1.25)(cylinder(r=1, h=1.5)))),
             forward(3.65 + self.wall_thickness)(
                 right(self.length + self.wall_thickness - 3.55)(up(self.wall_thickness + 1.25)(cylinder(r=1, h=1.5)))),
             forward(ww - 6 + self.wall_thickness)(
                 right(self.length + self.wall_thickness - 3.55)(up(self.wall_thickness + 1.25)(cylinder(r=1, h=1.5)))),
             forward(6.8)(up(self.wall_thickness + 2.75)(hole()(cube([self.wall_thickness, ww - 6.8 * 2, 1.5])))),
             forward(25.9 + self.wall_thickness)(
                 up(self.wall_thickness + 2.5)(right(7 + self.wall_thickness)(hole()(cube([8.1, 5.7, 3]))))),
             forward(25.9 + self.wall_thickness)(up(self.wall_thickness + 2.5)(right(20)(hole()(cube([8.1, 5.7, 3]))))),
             forward(self.width + self.wall_thickness * 2 - 7)(
                 up(self.wall_thickness + 2.75)(right(47.2)(hole()(cube([11.25, 7.55, 3.25]))))),
             forward(7.25 + self.wall_thickness)(up(self.wall_thickness + 2.75)(
                 right(self.length + self.wall_thickness)(hole()(cube([self.wall_thickness, 12, 3.2 - 1.5]))))),
             up(5 - self.wall_thickness / 2)(hole()(cube([lw, self.wall_thickness / 2, 5]))),
             up(5 - self.wall_thickness / 2)(hole()(cube([ww, self.wall_thickness / 2, 5]))),
             up(5 - self.wall_thickness / 2)(
                 forward(ww - self.wall_thickness / 2)(hole()(cube([lw, self.wall_thickness / 2, 5]))))]
        b = cube([lw, ww, self.wall_thickness])
        return b + a

    def top(self):
        lw = self.length + self.wall_thickness * 2
        ww = self.width + self.wall_thickness * 2
        a = [cube([lw, self.wall_thickness, 5]),
             cube([self.wall_thickness, ww, 5]),
             right(lw - self.wall_thickness)(cube([self.wall_thickness, ww, 5])),
             forward(ww - self.wall_thickness)(cube([lw, self.wall_thickness, 5])),
             forward(self.wall_thickness / 2)(right(self.wall_thickness / 2)(hole()(
                 cube([self.length + self.wall_thickness, self.width + self.wall_thickness, self.wall_thickness])))),
             ]
        b = up(5)(cube([lw, ww, self.wall_thickness]))
        return b + a


if __name__ == '__main__':
    _ = RaspwnCase()
    scad_render_to_file(_.bottom(), join('./out/', _.name + "bottom.scad"), file_header='$fn = 42;')
    scad_render_to_file(_.top(), join('./out/', _.name + "top.scad"), file_header='$fn = 42;')
