# prompt = "\nTell me which pizza topping would you like to have on your pizza?"
# prompt += "\nEnter 'quit' to stop."

# active = True
# while active:
#     message = input(prompt)

#     if message == 'quit':
#         active = False
#     else:
#         print(message)

while True:
    topping = input("\nEnter a pizza topping (or 'quit' to finish): ")
    if topping == 'quit':
        break
    print(f"Adding {topping} to your pizza!")