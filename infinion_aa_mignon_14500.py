from os.path import join

from solid.utils import *

SEGMENTS = 42
NAME = "infinion_aa_mignon_14500"


class InfinionAAMignon14500:
    diameter = 14
    height = 49
    nipple_diameter = 4.9
    nipple_height = 50.2 - height

    def __init__(self):
        pass

    def assemble(self):
        base = cylinder(d=self.diameter, h=self.height)
        base += up(self.height)(cylinder(d=self.nipple_diameter, h=self.nipple_height))
        return base


if __name__ == '__main__':
    scad_render_to_file(InfinionAAMignon14500().assemble(), join('./out/', NAME + ".scad"),
                        file_header='$fn = %s;' % SEGMENTS)
