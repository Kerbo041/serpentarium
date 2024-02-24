import random

def mass_x(u235_x):

    mass = {}
    u239_x = 1 - u235_x
    mm235 = 235
    mm238 = 238
    mmo2 = 32

    summ = mm235 * u235_x + mm238 * u239_x + mmo2

    m235 = round(mm235 * u235_x /summ, 5)
    m238 = round(mm238 *u239_x /summ, 5)
    mo2 = round(mmo2/summ, 5)

    check = m235 + m238 + mo2

    if check != 1:

        m238 = round(m238 + 0.00001, 5)

    mass["92235"] = m235
    mass["92238"] = m238
    mass["8016"] = mo2

    return mass


def mats_create(mass, iter):
    keys = mass.keys()
    red = int(150 * random.random())
    green = int(100 * random.random()) + 150
    blue = int(150 * random.random())

    out = "mat fuel" +str(iter) + " -10.45700 rgb " + str(red) + " " + str(green) + " " + str(blue) + "\n"
    for i in keys:
        out = out + i + ".09c   -" + str(mass[i]) + "\n"
    return out + "\n\n"

def materials(sections,materials):
    u235_x = []

    for i in range(sections):
        u235_x.append(float(materials[i]))

    mat_par = [mass_x(i) for i in u235_x]

    mats_out = ""
    mats_out += "% --- Zr-Nb cladding and shroud tube:\n\nmat clad    -6.55000 rgb 100 100 100\n40000.06c   -0.99000\n41093.06c   -0.01000\n\nmat tube    -6.58000 rgb 200 200 200\n40000.06c   -0.97500\n41093.06c   -0.02500\n\nmat wst -4.100 rgb 150 150 255 %12X18H10T\n6012.06c 0.00600\n26056.06c 0.34900\n24052.06c 0.09000\n28059.06c 0.05000\n22048.06c 0.00500\n8016.06c 0.44444\n1001.06c 0.05556\n\n\n% --- Water:\n\nmat water   -0.7207  moder lwtr 1001 rgb 0 0 255\n 1001.06c    2.0\n 8016.06c    1.0\n\n% --- UO2 fuel enriched to 3.6 wt-% U-235 with gd-64:\n\nmat fuel_gd   -10.45700 rgb 200 255 200\n92235.09c   -0.04103\n92238.09c   -0.79631\n64000.09c   -0.05000\n 8016.09c   -0.11266\n\n"
    for i in range(sections):
        mats_out += (mats_create(mat_par[i], i+1))
    
    return "% --- materials\n\n" + mats_out + "\n\n\n"