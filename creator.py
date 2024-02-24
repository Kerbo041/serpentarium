
from materials import materials
from geometry import geometry


def printer(name, str_out):
    fout = open(name, "w")
    print(str_out, file = fout)

def create(input_parameters):

    standart = open("standart", "r")
    standart_input = [line for line in standart.readlines()]

    sections = int(input_parameters[0])

    str_out = ""
    str_out += "% --- U49G6 Assembly --------------------------------------\n\n"
    str_out += materials(sections,input_parameters)
    str_out += geometry(sections)
    for line in standart_input:
        str_out += ( line + "\n")

    return str_out

def main():
    #choise = input("enter \"file\" if you want to read from file")
    
    parameters = open("parameters", "r")
    input_parameters = [float(line) for line in parameters.readlines()]

    printer("aaa8", create(input_parameters))
   
 
if __name__ == "__main__":
    main()
