threes = list(range(3,31,3))
for num in threes:
    print(num)
print(threes)

#list comprehension
thress_2 = [num*3 for num in range(1,11)]
print(thress_2)

#another method
three_3 =[]
for value in range(1,31):
    if value % 3 == 0:
        three_3.append(value)
print(three_3)