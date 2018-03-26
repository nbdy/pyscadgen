from os.path import join

from solid.utils import *

from esp8266 import ESP8266

FILE_HEADER = '$fn = %s;' % 42
NAME = "ES8266PCase"


# todo  outside module cases

class ES8266PCase:
    length = ESP8266.length
    width = ESP8266.width
    height = ESP8266.height

    def __init__(self, extra=6):
        self.esp = ESP8266()
        self.esp.btn_cylinder["height"] += extra
        self.esp.usb_port["length"] += extra
        self.esp.usb_port["left"] += extra
        self.length += extra
        self.width += extra
        self.height += extra
        self.extra = extra

    def generate_cable_slit(self):
        return hole()(forward(self.width / 2 - 3)(right(self.length - self.extra / 2)(cube([1, 6, self.height]))))

    def assemble(self):
        case = cube([self.length, self.width, self.height])
        case += right(self.extra / 2)(
            up(self.height / 2 - self.esp.height / 2)(forward(self.extra / 2)(hole()(ESP8266().assemble()))))
        case += hole()(cube([self.extra / 4, self.width, self.height]))
        case += self.generate_cable_slit()
        return case

    def upper_half(self):
        case = self.assemble()
        case += hole()(cube([self.length, self.width, self.height / 2]))
        return case

    def lower_half(self):
        case = self.assemble()
        case += up(self.height / 2)(hole()(cube([self.length, self.width, self.height / 2])))
        return case


if __name__ == '__main__':
    scad_render_to_file(ES8266PCase().lower_half(), join('./out/', NAME + "_lower.scad"), file_header=FILE_HEADER)
    scad_render_to_file(ES8266PCase().upper_half(), join('./out/', NAME + "_upper.scad"), file_header=FILE_HEADER)
