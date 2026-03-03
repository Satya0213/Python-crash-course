favorite_places ={
    'satyajeet': ['goa', 'manali', 'hyderabad'],
    'amit': ['pune', 'mumbai'],
    'aaishwarya': ['jaipur']
}

for name, places in favorite_places.items():
    if len(places) == 1:
        print(f"\n{name.title()}'s favorite place is:")
    
    else:
        print(f"\n{name.title()}'s favorites places are:")
    
    for place in places:
        print(f'-{place.title()}')