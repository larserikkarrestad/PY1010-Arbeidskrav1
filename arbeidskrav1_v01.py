"""
PY1010 - Arbeidskrav 1

@author: Lars-Erik Karrestad
"""

# Innledning

print("Dette programmet beregner totalkostnadene for elbil og bensinbil, samt årlig driftsdifferanse")
print("")
kmaar = float(input("Hvor mange km kjører du pr. år? "))

# Forsikringskostnader
forsikring_el = 5000
forsikring_bensin = 7500

# Trafikkforsikringskostnader
trafikkforsikring_dag = 8.38
trafikkforsikring_aar = trafikkforsikring_dag * 365

# Drivstoffkostnader
strompris = 2
drivstoff_el = 0.2 * kmaar * strompris
drivstoff_bensin = 1 * kmaar

# Bomutgifter
bomavgift_el = 0.1 * kmaar
bomavgift_bensin = 0.3 * kmaar

# Totale kostnader
totalkost_el = forsikring_el + trafikkforsikring_aar + drivstoff_el + bomavgift_el
totalkost_bensin = forsikring_bensin + trafikkforsikring_aar + drivstoff_bensin + bomavgift_bensin

# Differansen pr. år
differanse = totalkost_bensin - totalkost_el


print("Når du kjører ", kmaar, " km pr. år, så er utgiftene for elbil og bensinbil slik: ")
print("")
print("For elbil: ", totalkost_el)
print("For bensinbil: ", totalkost_bensin)
print("")
print("Kostnadsdifferansen pr. år er kr. ", differanse)
