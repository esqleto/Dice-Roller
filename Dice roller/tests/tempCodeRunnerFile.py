    if Force >= 0.1 and Force <= 10:
        break

Rolled = round((Force / 10) * 100)

header = [["Dices"], [] * Times]
for i in range(Times):
    header += ["balanco:" + str(i 