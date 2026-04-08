#--- version 1: Conditional test in the while statement ---
print('\n=== Version 1: Conditional in while ===')
topping = ""

while topping != 'quit':
    topping = input("Enter a topping (or 'quit' to finish): ")
    if topping != 'quit':
        print(f"Adding {topping} to your pizza!")

#--- version 2: Active (flag) version ---
print("\n=== Version 2: Active variable (flag)")
active = True
while active:
    topping = input("Enter a topping (or 'quit' to finish): ")
    if topping == 'quit':
        active = False
    else:
        print(f"Adding {topping} to your pizza!")

#--- version 3: break statement ---
print("=== Version 3: break statement ===")
while True:
    topping = input("Enter a topping (or 'quit' to finish): ")
    if topping == 'quit':
        break
    print(f"Adding {topping} to your pizza!")