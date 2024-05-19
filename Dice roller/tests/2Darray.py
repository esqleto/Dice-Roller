import random

rows, cols = (4,5)

arr = [[1]*cols]*rows
#arr[0][1] = 2
#for row in arr:
 #   print(row)
index = 0
Rolled = 3
for row in arr:
    for dice in range(Rolled):
        arr[index][dice] = random.randint(1,6)
        print(index)
        print(arr[index])
    index = index + 1