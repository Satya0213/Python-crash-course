#1 test
car = 'bmw'
print('Is car == "ford"? I predict False.')
print(car == "ford")

print('\nIs car == "bmw"? I predict True.')
print(car =='bmw')
print('---------------------------------------------')

#2 test
topping_req = 'pineapple'
print('\nIs topping_req == "pineapple"? I predict True')
print(topping_req == 'pineapple')

print('Is topping_req != "mushroom"? I predict True')
print(topping_req != 'mushroom')
print('---------------------------------------------')

#3 test
print('Can this couple marry?')
age_m = 22          #age of man
age_w = 20          #age of woman
print('Is age_m >= 21 and age_w >=18? I predict True')
print((age_m >= 21) and (age_w >=18))
print('You can marry.')

age_m = 48
age_w = 17
print("\nIs age_m >= 21 and age_w >= 18? I predict False")
print((age_m >= 21) and (age_w >=18))
print('You can not marry.')
print('---------------------------------------------')

#4 test
print('Can you go to school?')
age = 6
print("Is your age >= 6? I predict True")
print(age >= 6)
print('You can take admission in school.')

age = 2
print('\nIs your age >= 6? I predict False')
print(age >=6)
print("You can't take admission in school.")
print('---------------------------------------------')

#5 test
print('Top up your fuel')
low_fuel = 1                #low fuel level
current_fuel = 5            #vehicles fuel level
print('How much fuel is left: current_fuel <= low_fuel')
if current_fuel <= low_fuel:
    print('You need to refuel your vehicle.')
else:
    print('No need to refuel.')

low_fuel = 1
current_fuel = 0.5
print('How much fuel is left: current_fuel <= low_fuel')
if current_fuel <= low_fuel:
    print('You need to refuel your vehicle.')
else:
    print('No need to refuel.')