condition = 0

while condition < 10:
    condition = condition + 1
    if condition == 2:
        continue
    print(condition)
    if condition == 5:
        break
else:
    print("hi")
    pass