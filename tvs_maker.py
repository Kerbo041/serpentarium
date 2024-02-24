import random

def mass_x(u235_x):

    mass = {}
    u239_x = 1 - u235_x
    mm235 = 235
    mm238 = 238
    mmo2 = 32

    summ = mm235 * u235_x + mm238 * u239_x + mmo2

    m235 = round(mm235 * u235_x /summ, 5)
    m238 = round(mm238 *u239_x /summ, 5)
    mo2 = round(mmo2/summ, 5)

    check = m235 + m238 + mo2

    if check != 1:

        m238 = round(m238 + 0.00001, 5)

    mass["92235"] = m235
    mass["92238"] = m238
    mass["8016"] = mo2

    return mass


def mats_create(mass, iter):
    keys = mass.keys()
    red = int(150 * random.random())
    green = int(100 * random.random()) + 150
    blue = int(150 * random.random())
    out = ""
    out += "% --- UO2 fuel enriched to " "%"
    out += "mat fuel" +str(iter) + " -10.45700 rgb " + str(red) + " " + str(green) + " " + str(blue) + "\n"
    for i in keys:
        out += i + ".09c   -" + str(mass[i]) + "\n"
    return out + "\n\n"

def materials(sections,materials):
    u235_x = []

    for i in range(sections):
        u235_x.append(float(materials[i]))

    mat_par = [mass_x(i) for i in u235_x]

    mats_out = ""
    mats_out += "% --- Zr-Nb cladding and shroud tube:\n\nmat clad    -6.55000 rgb 100 100 100\n40000.06c   -0.99000\n41093.06c   -0.01000\n\nmat tube    -6.58000 rgb 200 200 200\n40000.06c   -0.97500\n41093.06c   -0.02500\n\nmat wst -4.100 rgb 150 150 255 %12X18H10T\n6012.06c 0.00600\n26056.06c 0.34900\n24052.06c 0.09000\n28059.06c 0.05000\n22048.06c 0.00500\n8016.06c 0.44444\n1001.06c 0.05556\n\n\n% --- Water:\n\nmat water   -0.7207  moder lwtr 1001 rgb 0 0 255\n 1001.06c    2.0\n 8016.06c    1.0\n\n% --- UO2 fuel enriched to 3.6 wt-% U-235 with gd-64:\n\nmat fuel_gd   -10.45700 rgb 200 255 200\n92235.09c   -0.04103\n92238.09c   -0.79631\n64000.09c   -0.05000\n 8016.09c   -0.11266\n\n"
    for i in range(sections):
        mats_out += (mats_create(mat_par[i], i+1))
    
    return "% --- materials\n\n" + mats_out + "\n\n\n"
def pin_create(iter):
    
    out = "pin " + str(iter) + "\n\n"
    out += "void   0.06\n"
    out += "fuel" +str(iter) + "   0.38000\n"
    out += "void   0.38650\n"
    out += "clad   0.45500\n"
    out += "water\n\n"

    return out



def pins(sections):

    pins_out = ""

    """
    standart_pins = open("standart_pins", "r")
    standart_pins_input = [line for line in standart_pins.readlines()]
    for line in standart_pins_input:
        pins_out += ( line + "\n")
    """
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

import re

def printer(name, str_out):
    fout = open(name, "w")
    print(str_out, file = fout)
    print("--------------------------------------\nfiles created\n--------------------------------------\n\n")

def create(input_parameters):
    #standart = open("standart", "r")
    #standart_input = [line for line in standart.readlines()]
    standart_input = "\n% --- Thermal scattering data for light water:\\n\\ntherm lwtr lwj3.11t\\n\\n% --- Cross section library file path:\\n\\nset acelib \"/home/viti/serpent/xs/jeff311/jeff311u.xsdata\"\\nset nfylib \"/home/viti/serpent/xs/jeff311/sss_jeff311.nfy\"\\nset declib \"/home/viti/serpent/xs/jeff311/sss_jeff311.dec\"\\n\\n\\n% --- Periodic boundary condition:\\n\\nset bc 3\\n\\n% --- Group constant generation:\\n\\n% universe = 0 (homogenization over all space)\\n% symmetry = 12\\n% 2-group structure (group boundary at 0.625 eV)\\n\\nset gcu  0\\nset sym  12\\nset nfg  2  0.625E-6\\n\\n% --- Neutron population and criticality cycles:\\n\\nset pop 5000 20 20\\n\\n% --- Geometry and mesh plots:\\n\\nplot 3 5000 5000\\nplot 2 5000 5000 0 -250 300\\nmesh 2 5000 5000\\nmesh 3 5000 5000"
    name = input_parameters[0]
    sections = int(input_parameters[1])
    mats = input_parameters[2:]

    str_out = ""
    str_out += "% variant: " + name + "\n"
    str_out += "% --- U49G6 Assembly --------------------------------------\n\n"
    str_out += materials(sections,mats)
    str_out += geometry(sections)
    #for line in standart_input:
    #    str_out += ( line + "\n")
    str_out += standart_input
    return str_out

def get_input():
    temp = input("enter the file name or print \"file\" to read input parameters from file\nPrint exit to stop programm\n")

    if temp == "file":
        if file_read():
            return True
        else:
            print("files dont created, try again\n")
        return True
    elif temp == "exit":
        return False
    else:
        try:
            temp_data = []
            name = temp
            temp_data.append(name)
            sections = int(input("enter the number of sections\n"))
            temp_data.append(sections)
            for i in range(sections):
                enrich = float(input("enrichment of " + str(i) + " section of tvs:\n"))
                temp_data.append(enrich)
            printer(name, create(temp_data))
            return True
        except:
            print("-------------------------------------\nerror in input parameters\n-------------------------------------\n\n")
            return True



def file_read():

    try:
        parameters = open("parameters.txt", "r")
    except:
        print("------------------------------\nno file, creating new\n------------------------------\n\n")
        parameters = open("parameters.txt", "w")
        print("name:%file_name%",file = parameters)
        print("%number of sections%",file = parameters)
        print("%enrichment for 1 section%",file = parameters)
        print("%enrichment for 2 section%",file = parameters)
        print("...",file = parameters)
        print("%enrichment for n section%",file = parameters)
        return False
    input_parameters = [line for line in parameters.readlines()]
    i = 0
    out = []
    try:
        while i <len(input_parameters):

            temp = []

            raw_name = str(input_parameters[i].split(":")[1])
            r_name = re.split(r'\s', raw_name)
            name = str(r_name[0])
            temp.append(name)
            i += 1
            sections = int(input_parameters[i])
            temp.append(sections)
            i += 1
            enr = []

            for j in range(sections):

                temp.append(float(input_parameters[i]))
                i+=1

            out.append(temp)
            for params in out:
                printer(params[0], create(params))
    except:
        print("------------------------------\nerror in input parameters\n------------------------------\n\n")

    return True
    

def main():
    i = True
    while i:
        i = get_input()
   
 
if __name__ == "__main__":
    main()