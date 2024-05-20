# Note: A lot of the comments are in portuguese because this is a university assignment.
# They will be removed later on.
import math
import random
import csv

output = open("CSVArray.csv", "w")
writer = csv.writer(output)

times = int(input("Digite o número de balanços: "))

dices = [[1] * times] * 100

while True:
    force = float(input("Digite a força aplicada(Entre 0.1 e 10): "))
    if force >= 0.1 and force <= 10:
        break

rolled = round((force / 10) * 100)

header = ["|Dados|"]
for i in range(times):
    header += ["|Balanço-" + str(i + 1) + "|"]

writer.writerow(header)

for row in range(100):
    if row < rolled:
        for dice in range(times):
            dices[row][dice] = random.randint(1, 6)
            print(dices[row])
    else:
        dices[row] = [1] * times

    writer.writerow(["Dado-" + str(row + 1)] + dices[row])

output.close()
