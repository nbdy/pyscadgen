from os.path import join

from solid.utils import *

from esp8266 import ESP8266

SEGMENTS = 42
NAME = "doorESPCase"


class DoorESPCase:
    length = ESP8266.length + 8
    width = ESP8266.width + 8
    height = ESP8266.height + 8

    def __init__(self):
        self.esp = ESP8266()

    def assemble(self):
        case = cube([self.length, self.width, self.height])
        case += hole()
        return case

    def lower_half(self):
        case = self.assemble()
        case += hole()(up(self.height / 2)(cube([self.length, self.width, self.height / 2])))
        return case

    def upper_half(self):
        case = self.assemble()
        case += hole()(cube([self.length, self.width, self.height / 2]))
        return case


if __name__ == '__main__':
    scad_render_to_file(DoorESPCase().assemble(), join('./out/', NAME + ".scad"), file_header='$fn = %s;' % SEGMENTS)
