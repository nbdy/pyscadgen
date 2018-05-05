from os.path import join
from solid.utils import *

from Case import Case
from Pin import Pin

SEGMENTS = 42

class FC22:
    name = "fc22"

    length = 31.95
    width = 19.85
    height = 1.3

    hole_diameter = 3.25
    hole_offset = 0.85 + hole_diameter / 2

    regulator_width = 7
    regulator_length = 6.8
    regulator_height = 6.35 - height
    regulator_offset_right = 5.8
    regulator_offset_forward = 0.6

    dual_diff_comp_width = 5.1
    dual_diff_comp_length = 5.5
    dual_diff_comp_height = 2.85 - height
    dual_diff_comp_offset_right = 7.8
    dual_diff_comp_offset_forward = 16.1 - dual_diff_comp_width

    pin_diameter = 2
    pin_length = 5

    sensor_height = 15.85
    sensor_base_diameter = 19.75
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
        o.append(up(self.height)(forward(self.width / 2)(rotate([180, 0, 0])(
            right(29.6 - self.sensor_base_diameter / 2)(cylinder(d=self.sensor_base_diameter,
                                                                 h=self.sensor_base_height))))))
        o.append(up(self.height - self.sensor_base_height)(forward(self.sensor_base_diameter / 2)(rotate([180, 0, 0])(
            right(29.6 - self.sensor_base_diameter / 2)(cylinder(d=self.sensor_top_base_diameter,
                                                                 h=self.sensor_height - self.sensor_base_height))))))
        o.append(up(self.height)(right(14)(cube([10.7, 2.65, 2.1 - self.height]))))
        o.append(up(self.height)(right(14)(forward(16.75)(cube([10.7, 2.65, 2.1 - self.height])))))
        o.append(up(self.height)(right(7.4)(forward(16.75)(cube([4.85, 2.6, 1.8 - self.height])))))
        o.append(up(self.height)(right(26.45)(forward(6.15)(cube([4.85, 8.35, 2.25])))))
        if self.has_pins:
            _p = Pin(pcb_height=self.height)
            p = up(Pin.base_width * 3 - self.height)(rotate([180, 0, 0])(_p.assemble()))
            for i in range(1, 5):
                o.append(down(2.5)(forward(5 + i * Pin.base_width)(right(2.5)(p))))
        return base + o


class FC22Case(Case):
    name = "fc22case"
    positive = FC22


if __name__ == '__main__':
    _ = FC22()
    scad_render_to_file(_.assemble(), join('./out/', _.name + ".scad"), file_header='$fn = 42;')
    _ = FC22Case()
    scad_render_to_file(_.assemble(), join('./out/', _.name + "_case.scad"), file_header='$fn = 42;')
    scad_render_to_file(_.bottom(), join('./out/', _.name + "_case_bottom.scad"), file_header='$fn = 42;')
    scad_render_to_file(_.top(), join('./out/', _.name + "_case_top.scad"), file_header='$fn = 42;')
    scad_render_to_file(_.connector.assemble(), join('./out/', _.name + "_connector.scad"), file_header='$fn = 42;')
