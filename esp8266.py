from os.path import join
from solid.utils import *

from Case import Case
from Pin import Pin

SEGMENTS = 42


class ESP8266:
    name = "esp8266"
    length = 57.5
    width = 31
    height = 1.6

    hole_diameter = 3.4

    usb_port = {
        "length": 5.7,
        "width": 7.9,
        "height": 2.7,
        "left": 5.7 - 4.65,
        "up": height,
        "forward": 11.8
    }

    usb_port_noose = {
        "width": 7.85,
        "height": 2.95,
        "down": (2.95 - usb_port["height"]) / 2,
        "back": (7.95 - usb_port["width"]) / 2
    }

    btn = {
        "length": 4,
        "width": 3,
        "height": 3.2 - height,
        "up": height,
        "right": 2
    }

    btn_cylinder = {
        "diameter": 1.5,
        "height": 3.65 - (btn["height"] + height),
        "up": height + btn["height"],
        "right": 4,
        "forward": 1.5
    }

    rst_btn = {
        "forward": 6
    }

    flash_btn = {
        "forward": 22
    }

    esp8266_base_chip = {
        "length": 24.2,
        "width": 16.2,
        "height": 2.4 - height,
        "forward": 23.75 - 16.2,
        "right": 57.95 - 24.2,
        "up": height
    }

    esp8266_chip = {
        "length": 15.15,
        "width": 12.10,
        "height": 4.65 - (height + esp8266_base_chip["height"]),
        "forward": (esp8266_base_chip["width"] - 12.05) / 2,
        "up": height + esp8266_base_chip["height"],
        "right": (esp8266_base_chip["length"] - 22.8)
    }

    electronics_plane = {
        "length": 27.5,
        "width": width - 5,
        "height": usb_port["height"],
        "forward": 2.5,
        "right": 6,
        "up": height
    }

    hole_offsets = [
        {"right": 1.25 + hole_diameter / 2, "forward": 1.3 + hole_diameter / 2},
        {"right": 1.25 + hole_diameter / 2, "forward": 26.4 + hole_diameter / 2},
        {"right": 53.2 + hole_diameter / 2, "forward": 1.3 + hole_diameter / 2},
        {"right": 53.2 + hole_diameter / 2, "forward": 26.4 + hole_diameter / 2}
    ]

    def __init__(self, has_pins=True):
        self.has_pins = has_pins

    def assemble(self):
        base = cube([self.length, self.width, self.height])

        _hole_cylinder = hole()(cylinder(d=self.hole_diameter, h=100, center=True))
        _holes = []
        for o in self.hole_offsets:
            _holes.append(right(o["right"])(forward(o["forward"])(_hole_cylinder)))

        base += _holes

        _o = []
        _cube_port = cube([self.usb_port["length"], self.usb_port_noose["width"], self.usb_port_noose["height"]])
        _o.append(
            forward(self.usb_port["forward"])(left(self.usb_port["left"])(up(self.height - 0.4)(
                _cube_port))))

        btn = right(self.btn["right"])(
            up(self.btn["up"])(cube([self.btn["length"], self.btn["width"], self.height])))
        btn += forward(self.btn_cylinder["forward"])(right(self.btn_cylinder["right"])(up(self.btn_cylinder["up"])(
            cylinder(d=self.btn_cylinder["diameter"], h=self.btn_cylinder["height"]))))
        _o.append(forward(self.rst_btn["forward"])(btn))
        _o.append(forward(self.flash_btn["forward"])(btn))

        _esp8266_chip = up(self.height)(cube([self.esp8266_base_chip["length"],
                                              self.esp8266_base_chip["width"],
                                              self.esp8266_base_chip["height"]]))
        _esp8266_chip += forward(self.esp8266_chip["forward"])(up(self.esp8266_chip["up"])(
            right(self.esp8266_chip["right"])(cube([self.esp8266_chip["length"],
                                                    self.esp8266_chip["width"],
                                                    self.esp8266_chip["height"]]))
        ))

        _o.append(forward(self.esp8266_base_chip["forward"])(right(self.esp8266_base_chip["right"])(_esp8266_chip)))
        _o.append(forward(self.electronics_plane["forward"])(
            up(self.electronics_plane["up"])(
                right(self.electronics_plane["right"])(
                    cube([self.electronics_plane["length"],
                          self.electronics_plane["width"],
                          self.electronics_plane["height"]])
                )
            )
        ))

        _o.append(up(self.height)(forward(25.5)(right(4.35)(cube([4.5, 3.3, 2.65 - self.height])))))

        if self.has_pins:
            p = Pin(pcb_height=self.height)
            for i in range(0, 15):
                _o.append(forward(0.25)(right(10 + i * p.base_width)(down(p.base_width)(p.assemble()))))
                _o.append(back(0.25)(right(10 + i * p.base_width)(
                    down(p.base_width)(forward(self.width - p.base_width)(p.assemble())))))

        base += _o

        return base


class ESP8266Case(Case):
    name = "esp8266case"
    positive = ESP8266

    def __init__(self):
        super(ESP8266Case, self).__init__(8)

    def finish(self, base):
        o = [
            left(self.wall_thickness)(up(self.positive.usb_port["up"])(forward(self.positive.usb_port["forward"])(
                hole()(cube([self.wall_thickness + self.positive.usb_port["length"],
                             self.positive.usb_port_noose["width"],
                             self.positive.usb_port["height"]]))))),
            down(1.25)(right(10)(hole()(cube([self.positive.length - 15, self.positive.width, 1.25])))),
            down(1.25)(
                right(self.positive.length - 15)(forward(self.positive.width / 2 - 9.5)(hole()(cube([15, 20, 1.25]))))),
            down(2.5)(forward(self.positive.width / 2 - 4.5)(right(self.positive.length)(hole()(
                cube([1, 10, self.wall_thickness * 2 + self.positive.height]))))),
            forward(self.positive.usb_port["forward"])(left(self.positive.usb_port["left"] + 10)(
                up(self.positive.usb_port["up"] - 2)(hole()(cube([self.positive.usb_port["length"] + 10,
                                                                  self.positive.usb_port_noose["width"],
                                                                  self.positive.usb_port_noose["height"]])))))
        ]
        return base + o


if __name__ == '__main__':
    _ = ESP8266
    scad_render_to_file(_().assemble(), join('./out/', _.name + ".scad"), file_header='$fn = 42;')
    _ = ESP8266Case()
    scad_render_to_file(_.bottom(), join('./out/', _.name + "_bottom.scad"), file_header='$fn = 42;')
    scad_render_to_file(_.top(), join('./out/', _.name + "_top.scad"), file_header='$fn = 42;')
    scad_render_to_file(_.connector.assemble(), join('./out/', _.name + "_connector.scad"), file_header='$fn = 42;')
