import random

def mass_x(u235_x):
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
    
    mass = {}

    mass["92235"] = m235
    mass["92238"] = m238
    mass["8016"] = mo2

    return mass


def materials_template(mass, iter, u235_x):

    keys = mass.keys()
    mass_235 = mass["92235"]
    mass_238 = mass["92238"]
    mass_8 = mass["8016"]

    red = int(150 * random.random())
    green = int(100 * random.random()) + 150
    blue = int(150 * random.random())

    template_file = open("template/materials_template", "r")

    mt_raw = template_file.read()

    template_file.close()

    mt_out = mt_raw.format(u235_x = u235_x, iter = iter, red = red, green = green, blue = blue, mass_235 = mass_235, mass_238 = mass_238, mass_8 = mass_8)

    return mt_out


def materials_default():
    default_file = open("default/materials_default", "r")
    md_out = default_file.read()
    default_file.close()
    return md_out

def materials(sections,materials):
    u235_x = []

    for i in range(sections):

        u235_x.append(float(materials[i]))

    mat_par = [mass_x(i) for i in u235_x]
    mats_out = "% --- materials\n\n"
    mats_out += materials_default()

    for i in range(sections):

        mats_out += (materials_template(mat_par[i], i+1, u235_x[i]))
    
    mats_out += "\n\n\n"

    return mats_out