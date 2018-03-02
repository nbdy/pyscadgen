from os.path import join

from solid.utils import *

SEGMENTS = 42
NAME = ""


# todo other antenna forms

class WiFiLinearAntenna:

    def __init__(self, mhz=[2400, 2500], mhz_range=None):
        if len(mhz) == 1:
            if mhz_range is None:
                exit("no mhz range nor second mhz array item")
            mhz = range(mhz[0], mhz[0] + mhz_range)
        else:
            mhz = range(mhz[0], mhz[1])
        self.mhz = mhz

    def calculate_average_length(self, min, max):
        return 5

    def assemble(self):
        base = cylinder(h=self.calculate_average_length())
        return base


if __name__ == '__main__':
    scad_render_to_file(WiFiLinearAntenna().assemble(), join('./out/', NAME + ".scad"),
                        file_header='$fn = %s;' % SEGMENTS)
