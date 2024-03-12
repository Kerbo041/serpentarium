from modules.interface.interface import interface
from modules.interface.console import get_input

def main():

    tk_on = True
    i = True
    while i:
        if tk_on == True:
            interface()
            i = False
        else:
            i = get_input()
   
 
if __name__ == "__main__":
    main()
