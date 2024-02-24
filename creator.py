
from materials import materials
from geometry import geometry
import re

def printer(name, str_out):
    fout = open(name, "w")
    print(str_out, file = fout)

def create(input_parameters):
    standart = open("standart", "r")
    standart_input = [line for line in standart.readlines()]
    name = input_parameters[0]
    sections = int(input_parameters[1])
    mats = input_parameters[2:]

    str_out = ""
    str_out += "% variant: " + name + "\n"
    str_out += "% --- U49G6 Assembly --------------------------------------\n\n"
    str_out += materials(sections,mats)
    str_out += geometry(sections)
    for line in standart_input:
        str_out += ( line + "\n")

    return str_out

def file_read():
    parameters = open("parameters", "r")
    input_parameters = [line for line in parameters.readlines()]
    i = 0
    out = []
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

    return out

def file_create(input_parameters):
    for params in input_parameters:
        printer(params[0], create(params))

def main():
    file_create(file_read())
   
 
if __name__ == "__main__":
    main()
