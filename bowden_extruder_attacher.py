from os.path import join
from solid.utils import *


class ExtruderAttacher:
    name = "attacher"
    icd = 12
    ich = 5.7
    ocd = 16.1
    och = 3
    h = ich + och * 2

    def __init__(self, extra=5):
        self.extra = extra
        self.wl = 12.5 + self.extra

    def assemble(self):
        return

    def front(self):
        a = cube([self.wl, self.wl, self.h])
        b = [right(self.wl / 2)(forward(self.wl / 2)(hole()(cylinder(h=self.och, d=self.ocd)))),
             right(self.wl / 2)(forward(self.wl / 2)(up(self.och)(hole()(cylinder(h=self.ich, d=self.icd))))),
             right(self.wl / 2)(
                 forward(self.wl / 2)(up(self.och + self.ich)(hole()(cylinder(h=self.och, d=self.ocd))))),
             forward(self.wl / 2)(hole()(cube([self.wl, self.wl / 2, self.h]))),
             left(1.5)(forward(self.wl / 2)(up(self.h / 2)(cube([3, self.wl, self.h / 5], center=True)))),
             right(self.wl + 1.5)(forward(self.wl / 2)(up(self.h / 2)(cube([3, self.wl, self.h / 5], center=True)))),
             left(1.5)(forward(self.wl / 4)(up(self.h / 2)(cube([3, self.wl / 2, self.h], center=True)))),
             right(self.wl + 1.5)(forward(self.wl / 4)(up(self.h / 2)(cube([3, self.wl / 2, self.h], center=True)))),
             forward(self.wl - self.extra / 2)(
                 left((39 - self.wl) / 2)(cube([(39 - self.wl) / 2, self.extra / 2, self.h]))),
             forward(self.wl - self.extra / 2)(right(self.wl)(cube([(39 - self.wl) / 2, self.extra / 2, self.h]))),
             left((39 - self.wl) / 2 - 4.5)(up(self.h / 2)(forward(self.wl - self.extra / 2)(
                 rotate([90, 0, 180])(hole()(cylinder(h=self.extra, d=3, center=True)))))),
             right(39 - (39 - self.wl) / 2 - 4.5)(up(self.h / 2)(forward(self.wl - self.extra / 2)(
                 rotate([90, 0, 180])(hole()(cylinder(h=self.extra, d=3, center=True)))))),
             forward(self.wl - self.extra / 2)(
                 up(self.h / 2 + (self.h / 5) / 2)(left(3)(hole()(cube([3, self.extra / 2, self.h / 2]))))),
             forward(self.wl - self.extra / 2)(
                 left(3)(hole()(cube([3, self.extra / 2, self.h / 2 - (self.h / 5) / 2])))),
             forward(self.wl - self.extra / 2)(
                 right(self.wl)(up(self.h / 2 + (self.h / 5) / 2)(hole()(cube([3, self.extra / 2, self.h / 2]))))),
             forward(self.wl - self.extra / 2)(
                 right(self.wl)(hole()(cube([3, self.extra / 2, self.h / 2 - (self.h / 5) / 2]))))]
        return a + b

    def back(self):
        a = left(3)(forward(self.wl / 2)(cube([self.wl + 6, self.wl / 2 + self.extra / 4, self.h])))
        b = [left(1.5)(forward(self.wl / 2)(up(self.h / 2)(hole()(cube([3, self.wl, self.h / 4], center=True))))),
             right(self.wl + 1.5)(
                 forward(self.wl / 2)(up(self.h / 2)(hole()(cube([3, self.wl, self.h / 4], center=True))))),
             right(self.wl / 2)(forward(self.wl / 2)(hole()(cylinder(h=self.och, d=self.ocd)))),
             right(self.wl / 2)(forward(self.wl / 2)(up(self.och)(hole()(cylinder(h=self.ich, d=self.icd))))),
             right(self.wl / 2)(
                 forward(self.wl / 2)(up(self.och + self.ich)(hole()(cylinder(h=self.och, d=self.ocd))))),
             right(self.wl / 2)(
                 forward(self.wl + self.extra / 4)(up(self.h / 2)(cube([39, self.extra / 4, self.h], center=True)))),
             left((39 - self.wl) / 2 - 4.5)(up(self.h / 2)(
                 forward(self.wl + 1)(rotate([90, 0, 180])(hole()(cylinder(h=self.extra / 2 + 1, d=3, center=True)))))),
             right(39 - (39 - self.wl) / 2 - 4.5)(up(self.h / 2)(
                 forward(self.wl + 1)(rotate([90, 0, 180])(hole()(cylinder(h=self.extra / 2 + 1, d=3, center=True))))))]
        return a + b


class MotorWasher:
    name = "MotorWasher"

    def __init__(self):
        self.h = 2
        self.wl = 42

    def assemble(self):
        b = cube([self.wl, self.wl, self.h])
        a = [forward(self.wl / 2)(right(self.wl / 2)(hole()(cylinder(d=22, h=self.h)))),
             forward(3 + 2.4)(right(3 + 2.4)(hole()(cylinder(d=6, h=self.h)))),
             forward(42 - (3 + 2.4))(right(3 + 2.4)(hole()(cylinder(d=6, h=self.h)))),
             forward(3 + 2.4)(right(42 - (3 + 2.4))(hole()(cylinder(d=6, h=self.h)))),
             forward(42 - (3 + 2.4))(right(42 - (3 + 2.4))(hole()(cylinder(d=6, h=self.h))))]
        return b + a


if __name__ == '__main__':
    _ = ExtruderAttacher()
    # scad_render_to_file(_.assemble(), join('./out/', _.name + ".scad"), file_header='$fn = 42;')
    scad_render_to_file(_.front(), join('./out/', _.name + "_front.scad"), file_header='$fn = 42;')
    scad_render_to_file(_.back(), join('./out/', _.name + "_back.scad"), file_header='$fn = 42;')
    _ = MotorWasher()
    scad_render_to_file(_.assemble(), join('./out/', _.name + ".scad"), file_header='$fn = 42;')
