pet_0 = {
    'type' : 'cat',
    'name' : 'bruno',
    'owners_name' : 'loius'
}

pet_1 = {
    'type' : 'dog',
    'name' : 'alex',
    'owners_name' : 'mike'
}

pet_2 = {
    'type' : 'cat',
    'name' : 'mikado',
    'owner_name' : 'negel'
}

pets = [pet_0, pet_1, pet_2]
for pet in pets:
    print('\nPet information')
    for key, value in pet.items():
        print(f'{key.title()}: {value.title()}')