favorite_number = {
    'aaishwarya' : [2, 10],
    'satyajeet' : [13, 8, 4],
    'shivam' : [18],
    'harsh' : [30, 15],
    }

for name,numbers in favorite_number.items():
    if len(numbers) ==1:
        print(f"\n{name.title()}'s favorite number is:")
    else:
        print(f"\n{name.title()}'s favorite numbers are:")
    
    for number in numbers:
        print(f'-{number}')