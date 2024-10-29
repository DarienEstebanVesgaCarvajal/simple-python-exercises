massAverage = 57
density = 1.038
specificHeat = 3.7
thermalConductivity = 5.4e-3
boilingTemp = 100
yolkMaxTemp = 70

originalTemp = float(input("What's the original temperature of the egg? (°C): "))

def log(x):
    return (x - 1) - (x - 1)**2 / 2 + (x - 1)**3 / 3 - (x - 1)**4 / 4 + (x - 1)**5 / 5

time = (massAverage ** (2/3) * specificHeat * density ** (1/3) * thermalConductivity * 
        3.14159 ** 2 * (4 * 3.14159 / 3) ** (2/3) *
        log((0.76 * originalTemp - boilingTemp) / (yolkMaxTemp - boilingTemp)))

print(f"The time needed in seconds to reach the maximum temperature is: {time}.")