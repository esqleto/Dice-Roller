import random
import csv

output = open("CSVArray.csv", "w")
writer = csv.writer(output)



rows, cols = (4,5)

arr = [[1]*cols]*rows

index = 0
Rolled = 3
for row in arr:
    for dice in range(Rolled):
        arr[index][dice] = random.randint(1,6)
    writer.writerow(arr[index])
    print(arr[index])
    index = index + 1
output.close()