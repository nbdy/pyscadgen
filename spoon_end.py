from os.path import join
from solid.utils import *

NAME = "spoon_end"


def assemble():
    small_x = {
        "l": 10.3,
        "w": 3.1,
        "h": 9.5
    }

    big_x = {
        "l": 5.9,
        "w": 11,
        "h": 9.5
    }

    cap_diameter = 19.2
    cap_height = 12

    o = forward(3.95)(cube([small_x["l"], small_x["w"], small_x["h"]]))
    o += right(small_x["l"] / 2 - big_x["l"] / 2)(cube([big_x["l"], big_x["w"], big_x["h"]]))
    o += forward(big_x["w"] / 2)(right(small_x["l"] / 2)(up(small_x["h"])(cylinder(d=cap_diameter, h=cap_height))))
    o += forward(big_x["w"] / 2)(right(small_x["l"] / 2)(up(small_x["h"] + cap_height)(sphere(d=cap_diameter))))
    o += forward(big_x["w"] / 2)(right(small_x["l"] / 2)(up(small_x["h"] + cap_height * 0.88)(
        left(cap_diameter - small_x["l"] / 2)(rotate([0, 90, 0])(
            hole()(cylinder(d=cap_diameter * 0.7, h=cap_diameter * 2)))))))

    o += back(5)(left(5)(up(big_x["h"] + 2)(hole()(cube([5, 20, 20])))))
    o += back(5)(right(small_x["l"])(up(big_x["h"] + 2)(hole()(cube([5, 20, 20])))))
    return o


if __name__ == '__main__':
    scad_render_to_file(assemble(), join('./out/', NAME + ".scad"), file_header='$fn = 42;')
