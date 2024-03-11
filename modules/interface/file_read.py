from  modules.file_gen.creator import creator
import re

def printer(name, str_out):
    fout = open("output/"+ name, "w")
    print(str_out, file = fout)
    print("--------------------------------------\nfiles created\n--------------------------------------\n\n")

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
                printer(params[0], creator(params))
    except:
        print("------------------------------\nerror in input parameters\n------------------------------\n\n")
