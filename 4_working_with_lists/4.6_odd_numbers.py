odd_no = list(range(1,21,2))
for number in odd_no:
    print(number)
print(odd_no)

#code using list comprehension
odd_no = [num for num in range(1,21) if num %2 != 0]
print(odd_no)