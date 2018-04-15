from os.path import join
from solid.utils import *


class Connector:
    connector_types = ["pin", "wall"]
    connector_head_types = {
        "pin": ["sphere"],
        "wall": ["hook", "t", "c", "z"]
    }

    # if pin length gets ignored
    def __init__(self, length=5, width=2, height=10, connector_type="pin", connector_head_type="sphere"):
        self.length = length
        self.width = width
        self.height = height
        if connector_head_type not in self.connector_head_types[connector_type]:
            print connector_head_type, "not in", self.connector_head_types[connector_type]
            exit(-1)
        self.connector = {
            'pin': self.pin_connector_assembly,
            'wall': self.wall_connector_assembly,
        }[connector_type]
        self.connector_head = {
            'sphere': self.sphere_connector_head,
            'hook': self.hook_connector_head,
            't': self.t_connector_head,
            'c': self.c_connector_head,
            'z': self.z_connector_head
        }[connector_head_type]

    def sphere_connector_head(self):
        return [up(self.height)(sphere(d=self.width + self.width / 2)),
                sphere(d=self.width + self.width / 2)]

    # todo remove hard-coded vars
    def hook_connector_head(self):
        return [up(self.height)(rotate([225, 0, 0])(cube([self.length, self.width, 1]))),
                forward(self.width)(up(self.height)(rotate([-135, 0, 0])(cube([self.length, self.width / 2, 2])))),
                rotate([45, 0, 0])(cube([self.length, self.width / 2, 2])),
                forward(self.width)(rotate([45, 0, 0])(cube([self.length, self.width, 1])))]

    # todo remove hard-coded variables
    def t_connector_head(self):
        return [up(self.height)(back(self.width)(cube([self.length, self.width * 3, 2]))),
                down(2)(back(self.width)(cube([self.length, self.width * 3, 2])))]

    # remove hard-coded variable
    def c_connector_head(self):
        return [up(self.height)(cube([self.length, self.width * 2, 2])),
                down(2)(cube([self.length, self.width * 2, 2]))]

    def z_connector_head(self):
        return [up(self.height)(cube([self.length, self.width * 2, 2])),
                down(2)(back(self.width)(cube([self.length, self.width * 2, 2])))]

    def pin_connector_assembly(self):
        return cylinder(h=self.height, d=self.width) + self.connector_head()

    def wall_connector_assembly(self):
        return cube([self.length, self.width, self.height]) + self.connector_head()

    def assemble(self):
        return self.connector()


if __name__ == '__main__':
    for t in Connector.connector_types:
        for k in Connector.connector_head_types[t]:
            print "rendering", t, k
            scad_render_to_file(Connector(connector_type=t, connector_head_type=k).assemble(),
                                join('./out/', "connector_" + t + "_" + k + ".scad"),
                                file_header='$fn = 42;')
