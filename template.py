from os.path import join
from solid.utils import *


class Template:
    name = "template"

    def __init__(self):
        pass

    def assemble(self):
        return


if __name__ == '__main__':
    _ = Template()
    scad_render_to_file(_.assemble(), join('./out/', _.name + ".scad"), file_header='$fn = 42;')
