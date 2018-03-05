from os.path import join

from solid.utils import *

from pin import Pin

SEGMENTS = 42
NAME = "esp8266"


class ESP8266:
    length = 57.5
    width = 31
    height = 1.5

    hole_diameter = 3

    usb_port = {
        "length": 5.7,
        "width": 7.4,
        "height": 2.4,
        "left": 1.5
    }

    btn = {
        "length": 4,
        "width": 3,
        "height": height,
        "up": 1.5,
        "right": 2
    }

    btn_cylinder = {
        "diameter": 1.5,
        "height": 1,
        "up": 2.5,
        "right": 4,
        "forward": 1.5
    }

    rst_btn = {
        "forward": 6
    }

    flash_btn = {
        "forward": 22
    }

    def __init__(self, has_pins=True):
        self.has_pins = has_pins

    def assemble(self):
        base = cube([self.length, self.width, self.height])

        _hole_cylinder = hole()(down(20)(cylinder(d=self.hole_diameter, h=100)))
        base += right(2)(forward(2)(_hole_cylinder))
        base += right(2)(forward(29)(_hole_cylinder))
        base += right(54.8)(forward(2)(_hole_cylinder))
        base += right(54.8)(forward(29)(_hole_cylinder))

        _cube_port = cube([self.usb_port["length"], self.usb_port["width"], self.usb_port["height"]])
        base += forward(self.width / 2 - self.usb_port["width"] / 2)(left(self.usb_port["left"])(_cube_port))

        btn = right(self.btn["right"])(
            up(self.btn["up"])(cube([self.btn["length"], self.btn["width"], self.height])))
        btn += forward(self.btn_cylinder["forward"])(right(self.btn_cylinder["right"])(up(self.btn_cylinder["up"])(
            cylinder(d=self.btn_cylinder["diameter"], h=self.btn_cylinder["height"]))))
        base += forward(self.rst_btn["forward"])(btn)
        base += forward(self.flash_btn["forward"])(btn)

        _cube_chip = cube([24.2, 16, 1])
        _cube_chip += forward(2)(right(1)(cube([15, 12, 1.2])))
        base += forward(7.6)(right(33.2)(up(1.5)(_cube_chip)))

        if self.has_pins:
            p = Pin()
            for i in range(0, 14):
                base += right(10 + i * p.base_width)(down(p.base_width)(p.assemble()))
                base += right(10 + i * p.base_width)(
                    down(p.base_width)(forward(self.width - p.base_width)(p.assemble())))

        return base


if __name__ == '__main__':
    scad_render_to_file(ESP8266().assemble(), join('./out/', NAME + ".scad"), file_header='$fn = %s;' % SEGMENTS)
