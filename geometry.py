def pin_create(iter):
    
    out = "pin " + str(iter) + "\n\n"
    out += "void   0.06\n"
    out += "fuel" +str(iter) + "   0.38000\n"
    out += "void   0.38650\n"
    out += "clad   0.45500\n"
    out += "water\n\n"

    return out



def pins(sections):
    pins_out = "% --- Central tube:\n\npin c\n\nwater  0.55\ntube   0.65\nwater   \n\n % --- Empty lattice position:\n\npin w\n\nwater \n  \n% --- fuel with Gd-64\n\npin g\n\nvoid 0.06\nfuel_gd   0.38000\nvoid   0.38650\nclad   0.45500\nwater   \n\npin t\n\nwst 0.45500\nwater\n\n %--- Fuel pins\n\n"
    for i in range(sections):
        pins_out += pin_create(i+1)
    return "% --- pins\n\n" + pins_out + "\n\n\n"




def lat_create(iter, a = 23):

    out = "lat l" + str(iter) + " 2  0.0 0.0 23 23 1.275\n"
    out += "w w w w w w w w w w w w w w w w w w w w w w w \n w w w w w w w w w w w {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} w \n  w w w w w w w w w w {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} w \n   w w w w w w w w w {i} {i} g {i} {i} {i} {i} {i} {i} {i} g {i} {i} w \n    w w w w w w w w {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} w \n     w w w w w w w {i} {i} {i} {i} {i} {i} {i} c {i} {i} {i} {i} {i} {i} {i} w \n      w w w w w w {i} {i} {i} {i} {i} c {i} {i} {i} {i} c {i} {i} {i} {i} {i} w \n       w w w w w {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} w \n        w w w w {i} {i} {i} {i} c {i} {i} {i} c {i} {i} {i} {i} c {i} {i} {i} {i} w \n          w w w {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} c {i} {i} {i} {i} {i} {i} {i} w \n          w w {i} {i} {i} {i} {i} {i} {i} c {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} w \n           w {i} {i} g {i} {i} c {i} {i} {i} {i} c {i} {i} {i} {i} c {i} {i} g {i} {i} w \n            w {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} c {i} {i} {i} {i} {i} {i} {i} w w \n             w {i} {i} {i} {i} {i} {i} {i} c {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} w w w \n              w {i} {i} {i} {i} c {i} {i} {i} {i} c {i} {i} {i} c {i} {i} {i} {i} w w w w \n              	w {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} w w w w w \n              	 w {i} {i} {i} {i} {i} c {i} {i} {i} {i} c {i} {i} {i} {i} {i} w w w w w w \n              	  w {i} {i} {i} {i} {i} {i} {i} c {i} {i} {i} {i} {i} {i} {i} w w w w w w w \n               	   w {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} w w w w w w w w \n              	    w {i} {i} g {i} {i} {i} {i} {i} {i} {i} g {i} {i} w w w w w w w w w \n              	     w {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} w w w w w w w w w w \n              	      w {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} {i} w w w w w w w w w w w \n              	       w w w w w w w w w w w w w w w w w w w w w w w \n"
    out += "\n\n\n"
    return out.format(i=iter)



def latence(sections):

    lats = ""
    lats += lat_create("t")

    for i in range(sections):

        lats += lat_create(i+1)

    return "% --- lats\n\n" + lats + "\n\n\n"




def surf_create(iter, height):

    surface = ""
    surface += "surf fuel_surf_" +str(iter) + "  pz  	" +  str(height) + " 	%fuel top\n"

    return surface




def surfaces(sections):

    surf_out = ""
    surf_out += "% --- Surfaces:\n\nsurf tvs_hex	hexyc	0.0  0.0  11.6625  	% Shroud tube inner radius\nsurf tvel_bottom  pz 	-188.5	%tvel bottom\nsurf tvel_top  pz  	210.7	%tvel top\nsurf tvs_bottom  pz 	-215.2 %tvs bottom\nsurf tvs_top  pz  	249.6	%tvs top\n"
    surf_out +="\nsurf fuel_top  pz  	184.0 	%fuel top\n"

    surf_need = sections + 1
    surf4cells = []
    surf4cells.append("fuel_bottom")
    if surf_need > 2:
        
        len = 368
        len_one = len / sections

        surf_numb = surf_need - 2
        surf_len = []

        for i in range(surf_numb):
            surf_len = (i+1) * len_one - len/2
            surf_out += surf_create(i+1,surf_len)
            surf4cells.append("fuel_surf_"+str(i+1))

    surf_out +="surf fuel_bottom  pz 	-184.0	%fuel bottom\n"

    surf_out += "\n\n\n"

    surf4cells.append("fuel_top")

    return [surf_out, surf4cells]



def cell_create(iter, bottom, top):
    cell_out = ""
    cell_out += "cell  tvel_section_" + str(iter) + "     0  fill l" + str(iter) + " -tvs_hex     " + bottom + "        -" + top + "	    % tvel section" + str(iter)  + " \n"
    return cell_out



def cells(sections, surf4cells):
    cells_out = ""
    cells_out += "% --- Cells:\n\ncell  tvel_bottom_zone  0  fill lt     -tvs_hex 	tvel_bottom     -fuel_bottom	% tvel bottom lattice\ncell  tvel_top_zone     0  fill lt     -tvs_hex     fuel_top        -tvel_top	    % tvel top lattice\ncell  tvs_bottom_zone   0  wst         -tvs_hex     tvs_bottom      -tvel_bottom    % tvs bottom\ncell  tvs_top_zone      0  wst         -tvs_hex     tvel_top        -tvs_top        % tvs top\ncell 99  0  outside                     tvs_hex 		                            % Outside world\ncell 98  0  outside                    -tvs_hex    -tvs_bottom		                % Outside world\ncell 97  0  outside                    -tvs_hex     tvs_top		                    % Outside world\n"
    for i in range(sections):
        cells_out += cell_create(i+1,surf4cells[i],surf4cells[i+1])
    return cells_out + "\n\n\n"



def geometry(sections):
    geometry_out = ""
    geometry_out += pins(sections)
    geometry_out += latence(sections)
    surfaces_out = surfaces(sections)
    geometry_out += surfaces_out[0]
    geometry_out += cells(sections, surfaces_out[1])
    return geometry_out