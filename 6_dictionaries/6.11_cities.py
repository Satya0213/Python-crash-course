cities = {
    'tokyo' : {
        'country' : 'japan',
        'population' : 37400000,
        'fact' : 'It is the most populous metroplitan area in the world.'
    },

    'paris' : {
        'country' : 'france',
        'population' : 11000000,
        'fact' : 'It is known as the City of Light.'
    },

    'mumbai' : {
        'country' : 'india',
        'population' : 20000000,
        'fact' : 'It is the financial capital of India.'
    }
}

for city, info in cities.items():
    print(f"\nCity: {city.title()}")
    
    print(f"Country: {info['country'].title()}")
    print(f"Population: {info['population']:,}")     # :, This is number formatting. 
                                                     # It adds commas to large numbers
                                                     # 37400000  37,400,000

    print(f"Fact: {info['fact']}")