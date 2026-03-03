rivers = {
    'nile river' : 'africa',
    'amazon river' : 'south america',
    'yangtze river' : 'china',
    'ganges river' : 'india',
    'indus river' : 'pakistan',
    'indus river' : 'india'
}

for river, country in rivers.items():
    print(f'The {river.title()} runs through {country.title()}.')

print("------------------------------------\n")

for river in set(rivers.keys()):
    print(river.title())

print("------------------------------------\n")

for country in sorted(rivers.values()):
    print(country.title())