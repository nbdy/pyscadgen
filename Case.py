from solid.utils import *

from Connector import ClipConnector


class Case(object):
    name = "case"
    positive = None
    connector = None

    def __init__(self, wall_thickness=4):
        self.wall_thickness = wall_thickness

    def generate_connectors(self, base):
        self.connector = ClipConnector(self.positive.length * 0.1,
                                       self.positive.width * 0.08,
                                       self.positive.height + self.wall_thickness,
                                       (self.positive.height + self.wall_thickness) * 0.12,
                                       (self.positive.width + self.wall_thickness) * 0.1,
                                       (self.positive.width + self.wall_thickness) * 0.02,
                                       (self.positive.width + self.wall_thickness) * 0.05)
        c = hole()(self.connector.assemble())
        _d = self.wall_thickness / 2 + ((self.positive.width + self.wall_thickness) * 0.02) / 2
        _b = self.wall_thickness / 2
        _f = self.wall_thickness / 2 + self.positive.width
        _t = self.positive.length * 0.1
        _r1 = (self.positive.length + self.wall_thickness) * 0.05
        _r2 = (self.positive.length + self.wall_thickness / 2) * 0.8
        return base + [
            down(_d)(back(_b)(right(_r1)(c))),
            down(_d)(forward(_f)(right(_r1 + _t)(rotate([0, 0, 180])(c)))),
            down(_d)(back(_b)(right(_r2)(c))),
            down(_d)(forward(_f)(right(_r2 + _t)(rotate([0, 0, 180])(c))))
        ]

    def finish(self, base):
        return base

    def assemble(self):
        b = back(self.wall_thickness / 2)(
            left(self.wall_thickness / 2)(down(self.wall_thickness / 2)(
                cube([self.positive.length + self.wall_thickness,
                      self.positive.width + self.wall_thickness,
                      self.positive.height + self.wall_thickness]))))
        return self.generate_connectors(self.finish(b + hole()(self.positive().assemble())))

    def bottom(self):
        return self.assemble() + hole()(
            back(self.wall_thickness / 2)(left(self.wall_thickness / 2)(up(self.positive.height / 2)(
                cube([self.positive.length + self.wall_thickness,
                      self.positive.width + self.wall_thickness,
                      self.positive.height + self.wall_thickness])))))

    def top(self):
        return self.assemble() + hole()(
            back(self.wall_thickness / 2)(
                left(self.wall_thickness / 2)(down(self.wall_thickness / 2 + self.positive.height / 2)(
                    cube([self.positive.length + self.wall_thickness,
                          self.positive.width + self.wall_thickness,
                          self.positive.height + self.wall_thickness / 2])))))
