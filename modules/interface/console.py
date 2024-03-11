from modules.file_gen.creator import creator
from  modules.interface.file_read import file_read
import re

def printer(name, str_out):
    fout = open("output/"+ name, "w")
    print(str_out, file = fout)
    print("--------------------------------------\nfiles created\n--------------------------------------\n\n")



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
        temp_data = []
        name = temp
        temp_data.append(name)
        sections = int(input("enter the number of sections\n"))
        temp_data.append(sections)
        for i in range(sections):
            enrich = float(input("enrichment of " + str(i+1) + " section of tvs:\n"))
            temp_data.append(enrich)
        printer(name, creator(temp_data))
        return True
        try:
            temp_data = []
            name = temp
            temp_data.append(name)
            sections = int(input("enter the number of sections\n"))
            temp_data.append(sections)
            for i in range(sections):
                enrich = float(input("enrichment of " + str(i+1) + " section of tvs:\n"))
                temp_data.append(enrich)
            printer(name, creator(temp_data))
            return True
        except:
            print("-------------------------------------\nerror in input parameters\n-------------------------------------\n\n")
            return True

    return True