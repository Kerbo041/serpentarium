
from materials import materials
from geometry import geometry
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
        parameters = open("parameters", "r")
    except:
        print("------------------------------\nno file, creating new\n------------------------------\n\n")
        parameters = open("parameters", "w")
        print("name:%file_name%",file = parameters)
        print("%number of sections",file = parameters)
        print("enrichment for 1 section",file = parameters)
        print("enrichment for 2 section",file = parameters)
        print("...",file = parameters)
        print("enrichment for n section",file = parameters)
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
