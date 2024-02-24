"""
for enrich
mass = {}
u235_x = 0.095
u239_x = 1 - u235_x
mm235 = 235
mm238 = 238
mmo2 = 32

summ = mm235 * u235_x + mm238 * u239_x + mmo2
print(summ)

m235 = round(mm235 * u235_x /summ, 5)
m238 = round(mm238 *u239_x /summ, 5)
mo2 = round(mmo2/summ, 5)

check = m235 + m238 + mo2

if check != 1:
    m238 = round(m238 + 0.00001, 5)
mass["92235"] = m235
mass["92238"] = m238
mass["8016"] = mo2

print(mass)

"""

pins_out = "% --- Central tube:\n\npin c\n\nwater  0.55\ntube   0.65\nwater   \n\n % --- Empty lattice position:\n\npin w\n\nwater \n  \n% --- fuel with Gd-64\n\npin g\n\nvoid 0.06\nfuel_gd   0.38000\nvoid   0.38650\nclad   0.45500\nwater   \n\npin t\n\nwst 0.45500\nwater\n\n %--- Fuel pins\n\n"
print(pins_out)