import math 

originalTemp = float(input("What's the original egg temperature?: "))
boilingTemp = 100 
yolkMaxTemp = 70  
massAverage = 57 
density = 1.038 
specificHeat = 3.7
thermalConductivity = 5.4 * math.pow(10, -3)

dividend = math.pow(massAverage, (2/3)) * (specificHeat * (math.pow(density, (1/3))))
divider = (thermalConductivity * math.pow(math.pi, 2)) * math.pow((4*math.pi)/3, (2/3))
resultDiv = dividend / divider

result = math.log(0.76 * (originalTemp - boilingTemp) / (yolkMaxTemp - boilingTemp))

seconds = resultDiv * result
minuts = round(seconds / 60)

print(f"The time needed in seconds to reach the maximum temperature is: {round(seconds)}.")