cubes = [value**3 for value in range(1,12)]
print(cubes)

print('\nThe first three items in the list are:')
print(cubes[0:3])

print('\nThe middle three items in the list are:')
middle_number = len(cubes)//2
middle_slice = cubes[middle_number-1:middle_number+2]
print(middle_slice)

print('\nThe last three items in the list are:')
last_slice= cubes[-3:]
print(last_slice)