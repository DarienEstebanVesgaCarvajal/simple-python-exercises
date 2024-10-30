massAverage = 57  # g
density = 1.038  # g/cm^3
specificHeat = 3.7  # J/g°C
thermalConductivity = 5.4e-3  # W/cm°C
boilingTemp = 100  # °C
yolkMaxTemp = 70  # °C

originalTemp = float(input("What's the original temperature of the egg? (°C): "))

logVolumen = (0.76 * originalTemp - boilingTemp) / (yolkMaxTemp - boilingTemp)

taylorSeries = (logVolumen - 1) - (logVolumen - 1)**2 / 2 + (logVolumen - 1)**3 / 3 - (logVolumen - 1)**4 / 4 + (logVolumen - 1)**5 / 5

time = (massAverage ** (2 / 3) * specificHeat * density ** (1 / 3)) / (thermalConductivity * 3.1416 ** 2) * (1 + taylorSeries)

print(f"The time needed in seconds to reach the maximum temperature is: {time}.")