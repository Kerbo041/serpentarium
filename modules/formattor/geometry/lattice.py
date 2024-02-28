
def lat_create(iter, a = 23):

    out = "lat l" + str(iter) + " 2  0.0 0.0 23 23 1.275\n"
    out += "w w w w w w w w w w w w w w w w w w w w w w w \n w w w w w w w w w w w {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} w \n  w w w w w w w w w w {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} w \n   w w w w w w w w w {i} {i} g {i} {i} {i} {i} {i} {i} {i} g {i} {i} w \n    w w w w w w w w {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} w \n     w w w w w w w {i} {i} {i} {i} {i} {i} {i} c {i} {i} {i} {i} {i} {i} {i} w \n      w w w w w w {i} {i} {i} {i} {i} c {i} {i} {i} {i} c {i} {i} {i} {i} {i} w \n       w w w w w {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} w \n        w w w w {i} {i} {i} {i} c {i} {i} {i} c {i} {i} {i} {i} c {i} {i} {i} {i} w \n          w w w {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} c {i} {i} {i} {i} {i} {i} {i} w \n          w w {i} {i} {i} {i} {i} {i} {i} c {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} w \n           w {i} {i} g {i} {i} c {i} {i} {i} {i} c {i} {i} {i} {i} c {i} {i} g {i} {i} w \n            w {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} c {i} {i} {i} {i} {i} {i} {i} w w \n             w {i} {i} {i} {i} {i} {i} {i} c {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} w w w \n              w {i} {i} {i} {i} c {i} {i} {i} {i} c {i} {i} {i} c {i} {i} {i} {i} w w w w \n              	w {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} w w w w w \n              	 w {i} {i} {i} {i} {i} c {i} {i} {i} {i} c {i} {i} {i} {i} {i} w w w w w w \n              	  w {i} {i} {i} {i} {i} {i} {i} c {i} {i} {i} {i} {i} {i} {i} w w w w w w w \n               	   w {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} w w w w w w w w \n              	    w {i} {i} g {i} {i} {i} {i} {i} {i} {i} g {i} {i} w w w w w w w w w \n              	     w {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} w w w w w w w w w w \n              	      w {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} w w w w w w w w w w w \n              	       w w w w w w w w w w w w w w w w w w w w w w w \n"
    out += "\n\n\n"
    return out.format(i=iter)



def lattice(sections):

    lats = ""
    lats += lat_create("t")

    for i in range(sections):

        lats += lat_create(i+1)

    return "% --- lats\n\n" + lats + "\n\n\n"