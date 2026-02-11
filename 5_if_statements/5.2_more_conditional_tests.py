#1_equality & unequality with string
my_name = 'Satyajeet'

#testes using lower() method
print(my_name.lower() == 'satyajeet')  #ture
print(my_name.lower() != 'satyajeet')    #false

print(my_name == 'satyjeet')            #false
print(my_name == 'aaishwarya')          #false
print(my_name != 'aaishwarya')          #true
print(my_name != 'satyajeet')           #true

#numerical test
#tested equality, greater than, less than, and operators
print("\nCan this couple marry?")
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

#or operator
username = 'user123'
email = 'user123@gmail.com'
input_field = 'user123'

if input_field == username or input_field == email:
    print('\nLogin successful')
else:
    print('Login credentials are incorrect')

#item in list?
my_list = ['wadapav', 'shev puri', 'spdp', 'pani puri']
if 'wadapav' in my_list:
    print('My fav food is in list.')
else:
    print('My fav food is not in list.')

#not in list?
bucket_list_destinations = ['manali', 'shimla','udaipur', 'kerla']
new_destination = 'goa'

if new_destination not in bucket_list_destinations:
    print('\nAdd new destination!!')
else:
    print('no need to modify list')