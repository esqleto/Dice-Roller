import statistics
import random
import csv

output = open("CSVArray.csv", "w")
output_chart = open("SumChart.csv", "w")
writer = csv.writer(output)
writer_chart = csv.writer(output_chart)

while True:
    force = float(input("Type the amount of force applied(between 0.1 and 10): "))
    if force >= 0.1 and force <= 10:
        break
while True:
    times = int(input("Type the amount of times that the tray should be shaken: "))
    if times > 0:
        break

dices = [[1] * times] * 100
dice_sum = [[0] * times] * 100
read = [[""] * times] * 100

rolled = round((force / 10) * 100)

header = ["|Dice|"]
for i in range(times):
    header += ["|Shake-" + str(i + 1) + "|"]
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
    else:
        dices[row] = [1] * times
        for rest in range(times):
            dice_sum[row][rest] += 1
            read[row][rest] = str(dices[row][rest]) + " | " + str(dice_sum[row][rest])

    writer.writerow(["Dice-" + str(row + 1)] + read[row])

writer.writerow(["|Sums|"] + dice_sum[99])
writer.writerow(["|Median|"] + [statistics.median(dice_sum[99])])
writer.writerow(["|Mean|"] + [statistics.mean(dice_sum[99])])
writer.writerow(["|Mode|"] + [statistics.mode(dice_sum[99])])

for i in range(times):
    writer_chart.writerow(["Sum of the shakes:" + str(i + 1)] + [dice_sum[99][i]])

output.close()
