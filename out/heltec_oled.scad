$fn = 42;

difference(){
	union() {
		cube(size = [27.2000000000, 27, 1]);
		translate(v = [0, 3, 0]) {
			translate(v = [2, 0, 0]) {
				translate(v = [0, 0, -20]) {
				}
			}
		}
	}
	/* Holes Below*/
	union(){
		translate(v = [0, 3, 0]){
			translate(v = [2, 0, 0]){
				translate(v = [0, 0, -20]){
					linear_extrude(height = 50, scale = [1, 1]) {
						circle(d = 2);
					}
				}
			}
		}
	} /* End Holes */ 
}
/***********************************************
*********      SolidPython code:      **********
************************************************
 
from os.path import join
from solid.utils import *

SEGMENTS = 42
HAS_PINS = True
PINS_BACKSIDE = False


def assemble():
    print "assembling"
    base = cube([27.2, 27, 1])

    print "punching holes"
    _cylinder_hole = down(20)(hole()(linear_extrude(50, scale=[3/2, 1])(circle(d=2))))
    base += forward(3)(right(2)(_cylinder_hole))

    return base


if __name__ == '__main__':
    scad_render_to_file(assemble(), join('./out/', "heltec_oled.scad"), file_header='$fn = %s;' % SEGMENTS)
 
 
************************************************/
