from solid.utils import *


class Case:
    positive = None

    def __init__(self, wall_thickness=4):
        self.wall_thickness = wall_thickness

    def assemble(self):
        b = back(self.wall_thickness / 2)(
            left(self.wall_thickness / 2)(down(self.wall_thickness / 2)(
                cube([self.positive.length + self.wall_thickness,
                      self.positive.width + self.wall_thickness,
                      self.positive.height + self.wall_thickness]))))
        return b + hole()(self.positive().assemble())

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
