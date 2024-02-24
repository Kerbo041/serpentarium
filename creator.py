
import materials
import geometry

def main():
    input = open("input/input", "w")

    standart = open("examples/standart", "r")
    standart_input = [line for line in standart.readlines()]

    parameters = open("parameters", "r")
    input_parameters = [float(line) for line in parameters.readlines()]

    sections = int(input_parameters[0])

    
    print("% --- U49G6 Assembly --------------------------------------\n\n", file = input)
    print("set title \"TVS\"\n", file = input)
    print(materials.materials(sections,input_parameters), file = input)
    print(geometry.geometry(sections), file = input)
    for i in standart_input:
        print(i, file = input)
    return 0

 
if __name__ == "__main__":
    main()
