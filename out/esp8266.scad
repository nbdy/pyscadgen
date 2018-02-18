$fn = 42;

difference(){
	union() {
		union() {
			union() {
				union() {
					union() {
						union() {
							union() {
								union() {
									union() {
										union() {
											cube(size = [57.5000000000, 31, 1.5000000000]);
											translate(v = [2, 0, 0]) {
												translate(v = [0, 2, 0]) {
												}
											}
										}
										translate(v = [2, 0, 0]) {
											translate(v = [0, 29, 0]) {
											}
										}
									}
									translate(v = [54.8000000000, 0, 0]) {
										translate(v = [0, 2, 0]) {
										}
									}
								}
								translate(v = [54.8000000000, 0, 0]) {
									translate(v = [0, 29, 0]) {
									}
								}
							}
							translate(v = [0, 12.1500000000, 0]) {
								translate(v = [-1.5000000000, 0, 0]) {
									cube(size = [5.7000000000, 7.4000000000, 2.4000000000]);
								}
							}
						}
						translate(v = [0, 6, 0]) {
							translate(v = [2, 0, 0]) {
								union() {
									translate(v = [0, 0, 1.5000000000]) {
										cube(size = [4, 3, 1.5000000000]);
									}
									translate(v = [0, 0, 2.5000000000]) {
										translate(v = [2, 0, 0]) {
											translate(v = [0, 1.5000000000, 0]) {
												cylinder(d = 1.5000000000, h = 1);
											}
										}
									}
								}
							}
						}
					}
					translate(v = [0, 22, 0]) {
						translate(v = [2, 0, 0]) {
							union() {
								translate(v = [0, 0, 1.5000000000]) {
									cube(size = [4, 3, 1.5000000000]);
								}
								translate(v = [0, 0, 2.5000000000]) {
									translate(v = [2, 0, 0]) {
										translate(v = [0, 1.5000000000, 0]) {
											cylinder(d = 1.5000000000, h = 1);
										}
									}
								}
							}
						}
					}
				}
				translate(v = [0, 7.6000000000, 0]) {
					translate(v = [33.2000000000, 0, 0]) {
						translate(v = [0, 0, 1.5000000000]) {
							union() {
								cube(size = [24.2000000000, 16, 1]);
								translate(v = [0, 2, 0]) {
									translate(v = [1, 0, 0]) {
										cube(size = [15, 12, 1.2000000000]);
									}
								}
							}
						}
					}
				}
			}
			translate(v = [0, 0, -8.5000000000]) {
				translate(v = [10, 0, 0]) {
					cube(size = [37.7000000000, 2.5000000000, 8.5000000000]);
				}
			}
		}
		translate(v = [0, 0, -8.5000000000]) {
			translate(v = [10, 0, 0]) {
				translate(v = [0, 28.6000000000, 0]) {
					cube(size = [37.7000000000, 2.5000000000, 8.5000000000]);
				}
			}
		}
	}
	/* Holes Below*/
	union(){
		union(){
			union(){
				union(){
					union(){
						union(){
							union(){
								union(){
									union(){
										union(){
											translate(v = [2, 0, 0]){
												translate(v = [0, 2, 0]){
													translate(v = [0, 0, -20]) {
														cylinder(d = 3, h = 100);
													}
												}
											}
										}
										translate(v = [2, 0, 0]){
											translate(v = [0, 29, 0]){
												translate(v = [0, 0, -20]) {
													cylinder(d = 3, h = 100);
												}
											}
										}
									}
									translate(v = [54.8000000000, 0, 0]){
										translate(v = [0, 2, 0]){
											translate(v = [0, 0, -20]) {
												cylinder(d = 3, h = 100);
											}
										}
									}
								}
								translate(v = [54.8000000000, 0, 0]){
									translate(v = [0, 29, 0]){
										translate(v = [0, 0, -20]) {
											cylinder(d = 3, h = 100);
										}
									}
								}
							}
						}
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


def assemble():
    print "assembling"
    base = cube([57.5, 31, 1.5])

    print "punching holes"
    _hole_cylinder = hole()(down(20)(cylinder(d=3, h=100)))
    base += right(2)(forward(2)(_hole_cylinder))
    base += right(2)(forward(29)(_hole_cylinder))
    base += right(54.8)(forward(2)(_hole_cylinder))
    base += right(54.8)(forward(29)(_hole_cylinder))

    print "attaching usb port"
    _cube_port = cube([5.7, 7.4, 2.4])
    base += forward(31/2-5.7/2)(left(1.5)(_cube_port))

    print "attaching buttons"
    _cube_btn = up(1.5)(cube([4, 3, 1.5]))
    _cube_btn += up(2.5)(right(2)(forward(1.5)(cylinder(d=1.5, h=1))))
    base += forward(6)(right(2)(_cube_btn))
    base += forward(22)(right(2)(_cube_btn))

    print "attaching main chip"
    _cube_chip = cube([24.2, 16, 1])
    _cube_chip += forward(2)(right(1)(cube([15, 12, 1.2])))
    base += forward(7.6)(right(33.2)(up(1.5)(_cube_chip)))

    if HAS_PINS:
        print "attaching pins"
        pin_base = cube([37.7, 2.5, 8.5])
        # todo pins
        base += down(8.5)(right(10)(pin_base))
        base += down(8.5)(right(10)(forward(28.6)(pin_base)))

    print "done"
    return base


if __name__ == '__main__':
    scad_render_to_file(assemble(), join('./out/', "esp8266.scad"), file_header='$fn = %s;' % SEGMENTS)
 
 
************************************************/
