from os.path import join
from solid.utils import *

from Case import Case
from pin import Pin

SEGMENTS = 42
NAME = "fc22"


class FC22:
    length = 31.8
    width = 19.75
    height = 1.3

    hole_diameter = 3.25
    hole_offset = 0.85 + hole_diameter / 2

    regulator_width = 6.95
    regulator_length = 6.8
    regulator_height = 6.35 - height
    regulator_offset_right = 5.8
    regulator_offset_forward = 12.3

    dual_diff_comp_width = 4.9
    dual_diff_comp_length = 4
    dual_diff_comp_height = 2.85 - height
    dual_diff_comp_offset_right = 7.8
    dual_diff_comp_offset_forward = 8.8 - dual_diff_comp_width

    pin_diameter = 1
    pin_length = 5

    sensor_height = 15.85
    sensor_base_diameter = 19.5
    sensor_base_height = 6.9
    sensor_top_base_diameter = 15.5
    sensor_top_diameter = 12.6

    def __init__(self, has_pins=True, pins_bent=False):
        self.has_pins = has_pins
        self.pins_bent = pins_bent

    def assemble(self):
        base = cube([self.length, self.width, self.height])
        h = hole()(cylinder(h=self.height, d=self.hole_diameter))
        o = [forward(self.hole_offset)(right(self.hole_offset)(h)),
             forward(self.width - self.hole_offset)(right(self.hole_offset)(h)),
             forward(self.hole_offset)(right(self.length - self.hole_offset)(h)),
             forward(self.width - self.hole_offset)(right(self.length - self.hole_offset)(h))]

        o.append(up(self.height)(forward(self.regulator_offset_forward)(right(self.regulator_offset_right)(
            cube([self.regulator_length, self.regulator_width, self.regulator_height])
        ))))
        o.append(up(self.height)(forward(self.dual_diff_comp_offset_forward)(right(self.dual_diff_comp_offset_right)(
            cube([self.dual_diff_comp_length, self.dual_diff_comp_width, self.dual_diff_comp_height])
        ))))
        p = up(self.height)(cylinder(h=self.pin_length, d=self.pin_diameter))
        o.append(forward(7.5)(right(17.3)(p)))
        o.append(forward(6)(right(20.7)(p)))
        o.append(forward(7.5)(right(24)(p)))
        o.append(forward(14)(right(17.3)(p)))
        o.append(forward(15.25)(right(20.7)(p)))
        o.append(forward(14)(right(24)(p)))
        o.append(up(self.height)(forward(self.sensor_base_diameter / 2)(rotate([180, 0, 0])(
            right(29.6 - self.sensor_base_diameter / 2)(cylinder(d=self.sensor_base_diameter,
                                                                 h=self.sensor_base_height))))))
        o.append(up(self.height - self.sensor_base_height)(forward(self.sensor_base_diameter / 2)(rotate([180, 0, 0])(
            right(29.6 - self.sensor_base_diameter / 2)(cylinder(d=self.sensor_top_base_diameter,
                                                                 h=self.sensor_height - self.sensor_base_height))))))
        if self.has_pins:
            p = up(Pin.base_width * 3 - self.height)(rotate([180, 0, 0])(Pin(pcb_height=self.height).assemble()))
            for i in range(1, 5):
                o.append(down(2.5)(forward(5 + i * Pin.base_width)(right(2.5)(p))))
        return base + o


class FC22Case(Case):
    positive = FC22


if __name__ == '__main__':
    scad_render_to_file(FC22().assemble(), join('./out/', NAME + ".scad"), file_header='$fn = 42;')
    scad_render_to_file(FC22Case().assemble(), join('./out/', NAME + "_case.scad"), file_header='$fn = 42;')
    scad_render_to_file(FC22Case().bottom(), join('./out/', NAME + "_case_bottom.scad"), file_header='$fn = 42;')
    scad_render_to_file(FC22Case().top(), join('./out/', NAME + "_case_top.scad"), file_header='$fn = 42;')
