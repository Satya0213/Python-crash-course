#Start with the list you used in Exercise 3-1, but instead of just 
#printing each person’s name, print a message to them. The text of each mes￾sage should be the same, but each message should be personalized with the 
#person’s name.

names = ['Harsh Pawar', 'shivtej thorat', 'shivam tarate', 'rutuja shinde']
message = 'How are you'
print(f"{message}, {names[-1].title()}?")
print(f'{message}, {names[0].title()}?')
print(f'{message}, {names[1].title()}?')
print(f'{message}, {names[2].title()}?')