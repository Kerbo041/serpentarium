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

print(range(-1))