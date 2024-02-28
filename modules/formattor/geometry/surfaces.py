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