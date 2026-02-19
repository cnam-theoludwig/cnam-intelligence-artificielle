values: list[int] = [10, 4, 6, 3, 89, 45]

values.sort()
print(values)

for i in range(len(values)):
    values[i] = values[i] ** 2

print(values)
