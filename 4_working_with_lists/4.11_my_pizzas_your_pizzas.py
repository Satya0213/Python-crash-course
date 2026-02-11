my_pizzas = ['margarita', 'extra vaganza', 'farmhouse']  #original list
friends_pizzas = my_pizzas[:]                           #copy of original list

#print(my_pizzas)
#print(friends_pizzas)

#for pizza in my_pizzas:
#    print(pizza)

my_pizzas.append("italian")             #new value added to original list
friends_pizzas.append('pepperoni')      #new value added to copy of original list

print('My favorite pizzas are:')
for pizza in my_pizzas:
    print(pizza.title())

print('\nFriends favorite pizzas are:')
for pizza in friends_pizzas:
    print(pizza.title())