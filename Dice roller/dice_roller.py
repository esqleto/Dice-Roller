# Note: A lot of the comments are in portuguese because this is a university assignment.
# They will be removed later on.
import math
import random
import csv

output = open("CSVArray.csv", "w")
writer = csv.writer(output)

while True:
    force = float(input("Digite a força aplicada(Entre 0.1 e 10): "))
    if force >= 0.1 and force <= 10:
        break

times = int(input("Digite o número de balanços: "))

dices = [[1] * times] * 100
dice_sum = [[0] * times] * 100
read = [[""] * times] * 100

rolled = round((force / 10) * 100)

header = ["|Dados|"]
for i in range(times):
    header += ["|Balanço-" + str(i + 1) + "|"]

writer.writerow(header)

for row in range(100):
    if row < rolled:
        for dice in range(times):

            dices[row][dice] = random.randint(1, 6)

            if row > 0:
                dice_sum[row][dice] += dices[row][dice]
                read[row][dice] = (
                    str(dices[row][dice]) + " | " + str(dice_sum[row][dice])
                )
            else:
                dice_sum[row][dice] += dices[row][dice]
                read[row][dice] = str(dices[row][dice]) + " | " + str(dices[row][dice])

            print(dices[row])
    else:
        dices[row] = [1] * times
        for rest in range(times):
            dice_sum[row][rest] += 1
            read[row][rest] = str(dices[row][rest]) + " | " + str(dice_sum[row][rest])

    writer.writerow(["Dado-" + str(row + 1)] + read[row])

writer.writerow(["|Somas|"] + dice_sum[99])

output.close()