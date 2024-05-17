#Note: A lot of the comments are in portuguese because this is a university assignment.
#They will be removed later on.
import math
import random

Dices = []
for i in range(100):
    Dices.append(i)
    Dices[i] = 1 

Times = int(input("Digite o numero de balancos: "))

while True:
    Force = float(input("Digite a Forca aplicada(Entre 0.1 e 10): "))
    if Force >= 0.1 and Force <= 10:
        break

Rolled = (Force/10) * 100

for turn in range(Times):
    for dice in range(round(Rolled)):
        Dices[dice] = random.randint(1,6)
        print(Dices[dice])



