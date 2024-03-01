from modules.interface.interface import interface
from modules.interface.console import get_input

def main():

    tk_on = False
    i = True
    while i:
        if tk_on == True:
            i = interface()
        else:
            i = get_input()
   
 
if __name__ == "__main__":
    main()
