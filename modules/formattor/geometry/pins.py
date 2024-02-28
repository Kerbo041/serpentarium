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