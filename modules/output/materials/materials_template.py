import random
import calculator
#materials_template
def mats_create(mass, iter, u235_x):
    keys = mass.keys()
    red = int(150 * random.random())
    green = int(100 * random.random()) + 150
    blue = int(150 * random.random())
    out = ""
    out += "% --- UO2 fuel enriched to " + str(u235_x*100) +  "%\n"
    out += "mat fuel" +str(iter) + " -10.45700 rgb " + str(red) + " " + str(green) + " " + str(blue) + "\n"
    for i in keys:
        out += i + ".09c   -" + str(mass[i]) + "\n"
    return out + "\n\n"