array = [10, 5, 2, 8]

print(array)
print(array[1])
print(array[:])
print(array[:3])
print(array[1:3])
print(array[-1])
print(array[:-1])
print(array[:-2])
print(array[-5:-2])

array[2] = 1111
print(array)

maximum = array[0]
for num in array:
    if num > maximum:
        maximum = num
print(maximum)

minimum = array[0]
for num in array:
    if num < minimum:
        minimum = num
print(minimum)
