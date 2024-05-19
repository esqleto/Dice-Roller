#Note: A lot of the comments are in portuguese because this is a university assignment.
#They will be removed later on.
import math
import random
import csv

Times = int(input("Digite o numero de balancos: "))

Dices = [[1] * Times] * 100

while True:
    Force = float(input("Digite a Forca aplicada(Entre 0.1 e 10): "))
    if Force >= 0.1 and Force <= 10:
        break

Rolled = round((Force/10) * 100)

for turn in range(Times):
    for dice in range(Rolled):
        Dices[dice] = random.randint(1,6)
        print(Dices[dice])



