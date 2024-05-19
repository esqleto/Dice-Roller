import csv

#data = [[10,20,30],[40,50,60],[70,80,90]]
Dices = []
for i in range(100):
    Dices.append(i)
    Dices[i] = [1] 

file = open("CSVFile.csv", "w")

writer = csv.writer(file)

for row in Dices:
    print(row)
    writer.writerow(row)
file.close()