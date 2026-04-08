while True:
    age = input("Enter your age (or 'quit' to exit): ")
    if age == 'quit':
        break

    age = int(age)
    if age < 3:
        print("Ticket fee: Free")
    elif 3 < age < 12:
        print("Ticket fee: $10")
    elif age > 12:
        print("Ticket fee: $15")
