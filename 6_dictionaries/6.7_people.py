person_information_0 = {
    'first' : 'harvey',
    'last' : 'spectar',
    'location' : 'new york'
}

person_information_1 = {
    'first' : 'mike',
    'last' : 'ross',
    'location' : 'boston'
}

person_information_2 = {
    'first' : 'donna',
    'last' : 'paulison',
    'location' : 'chiago'

}

people = [person_information_0, person_information_1, person_information_2]
for person in people:
    print('\nPerson details.')
    for key, value in person.items():
        print(f'{key.title()}: {value.title()}')

# another method
# for person in people:
#      print("\nHere is what I know about this person:")
#      print(f"First Name: {person['first_name'].title()}")
#      print(f"Last Name: {person['last_name'].title()}")
#      print(f"Age: {person['age']}")
#      print(f"City: {person['city'].title()}")