from os.path import join

from solid.utils import *

from sd_card import SDCard

SEGMENTS = 42
NAME = "sd_holder.scad"


class SDCardHolder:
    def __init__(self, slots=10):
        self.sd_card = SDCard(1)
        self.slots = slots

    def generate_steps(self):
        s = 0
        for i in range(0, self.slots):
            if i == 0:
                s += 2
            else:
                s += self.sd_card.height
                s += 2
            yield s

    def assemble(self):
        base = cube([self.sd_card.height * self.slots + self.slots * 2 + 2,
                     self.sd_card.width + 4,
                     self.sd_card.length / 1.8])
        slot = forward(2)(up(2)(rotate([90, 0, 90])(self.sd_card.assemble())))
        for s in self.generate_steps():
            base += right(s)(hole()(slot))

        return base


if __name__ == '__main__':
    scad_render_to_file(SDCardHolder().assemble(), join('./out/', NAME), file_header='$fn = %s;' % SEGMENTS)
