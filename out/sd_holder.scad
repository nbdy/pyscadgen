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
											cube(size = [53.0000000000, 28.8000000000, 18.2222222222]);
											translate(v = [2, 0, 0]) {
											}
										}
										translate(v = [7.1000000000, 0, 0]) {
										}
									}
									translate(v = [12.2000000000, 0, 0]) {
									}
								}
								translate(v = [17.3000000000, 0, 0]) {
								}
							}
							translate(v = [22.4000000000, 0, 0]) {
							}
						}
						translate(v = [27.5000000000, 0, 0]) {
						}
					}
					translate(v = [32.6000000000, 0, 0]) {
					}
				}
				translate(v = [37.7000000000, 0, 0]) {
				}
			}
			translate(v = [42.8000000000, 0, 0]) {
			}
		}
		translate(v = [47.9000000000, 0, 0]) {
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
												translate(v = [0, 2, 0]) {
													translate(v = [0, 0, 2]) {
														rotate(a = [90, 0, 90]) {
															cube(size = [24.8000000000, 32.8000000000, 3.1000000000]);
														}
													}
												}
											}
										}
										translate(v = [7.1000000000, 0, 0]){
											translate(v = [0, 2, 0]) {
												translate(v = [0, 0, 2]) {
													rotate(a = [90, 0, 90]) {
														cube(size = [24.8000000000, 32.8000000000, 3.1000000000]);
													}
												}
											}
										}
									}
									translate(v = [12.2000000000, 0, 0]){
										translate(v = [0, 2, 0]) {
											translate(v = [0, 0, 2]) {
												rotate(a = [90, 0, 90]) {
													cube(size = [24.8000000000, 32.8000000000, 3.1000000000]);
												}
											}
										}
									}
								}
								translate(v = [17.3000000000, 0, 0]){
									translate(v = [0, 2, 0]) {
										translate(v = [0, 0, 2]) {
											rotate(a = [90, 0, 90]) {
												cube(size = [24.8000000000, 32.8000000000, 3.1000000000]);
											}
										}
									}
								}
							}
							translate(v = [22.4000000000, 0, 0]){
								translate(v = [0, 2, 0]) {
									translate(v = [0, 0, 2]) {
										rotate(a = [90, 0, 90]) {
											cube(size = [24.8000000000, 32.8000000000, 3.1000000000]);
										}
									}
								}
							}
						}
						translate(v = [27.5000000000, 0, 0]){
							translate(v = [0, 2, 0]) {
								translate(v = [0, 0, 2]) {
									rotate(a = [90, 0, 90]) {
										cube(size = [24.8000000000, 32.8000000000, 3.1000000000]);
									}
								}
							}
						}
					}
					translate(v = [32.6000000000, 0, 0]){
						translate(v = [0, 2, 0]) {
							translate(v = [0, 0, 2]) {
								rotate(a = [90, 0, 90]) {
									cube(size = [24.8000000000, 32.8000000000, 3.1000000000]);
								}
							}
						}
					}
				}
				translate(v = [37.7000000000, 0, 0]){
					translate(v = [0, 2, 0]) {
						translate(v = [0, 0, 2]) {
							rotate(a = [90, 0, 90]) {
								cube(size = [24.8000000000, 32.8000000000, 3.1000000000]);
							}
						}
					}
				}
			}
			translate(v = [42.8000000000, 0, 0]){
				translate(v = [0, 2, 0]) {
					translate(v = [0, 0, 2]) {
						rotate(a = [90, 0, 90]) {
							cube(size = [24.8000000000, 32.8000000000, 3.1000000000]);
						}
					}
				}
			}
		}
		translate(v = [47.9000000000, 0, 0]){
			translate(v = [0, 2, 0]) {
				translate(v = [0, 0, 2]) {
					rotate(a = [90, 0, 90]) {
						cube(size = [24.8000000000, 32.8000000000, 3.1000000000]);
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
 
 
************************************************/
