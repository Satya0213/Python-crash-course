number = input('Enter any number, I will tell you is it multiple of 10 or not. ')
number = int(number)
if number % 10 == 0:
    print(f"{number} is multiple of ten.")
else:
    print(f"{number} is not multiple of ten.")