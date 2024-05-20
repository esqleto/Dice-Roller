# Note: A lot of the comments are in portuguese because this is a university assignment.
# They will be removed later on.
import math
import random
import csv

output = open("CSVArray.csv", "w")
writer = csv.writer(output)

Times = int(input("Digite o numero de balancos: "))

Dices = [[1] * Times] * 100

while True:
    Force = float(input("Digite a Forca aplicada(Entre 0.1 e 10): "))
    if Force >= 0.1 and Force <= 10:
        break

Rolled = round((Force / 10) * 100)

for row in range(100):
    if row < Rolled:
        for dice in range(Times):
            Dices[row][dice] = random.randint(1, 6)
            print(Dices[row])
    else: 
        Dices[row] = [1] * Times

    writer.writerow([row])
    writer.writerow(Dices[row])
    
output.close()