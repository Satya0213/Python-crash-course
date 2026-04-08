sandwich_orders = ['tuna', 'pastrami', 'chicken', 'pastrami', 'egg salad', 'pastrami', 'club']
finished_sandwiches = []

print('Sorry we have run out of pastrami.\n')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

print("\nThe following sandwiches were made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")