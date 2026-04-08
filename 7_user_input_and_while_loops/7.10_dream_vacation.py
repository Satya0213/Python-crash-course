responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    destination = input("Which is your dream vacation destination? ")
    responses[name] = destination
    
    repeat = input("Would you like to tell another person respond? (yes/ no) ")
    
    if repeat == 'no':
        polling_active = False

print("\n--- Dream destination ---")
for name,destination in responses.items():
    print(f"{name} would love to visit {destination}.")