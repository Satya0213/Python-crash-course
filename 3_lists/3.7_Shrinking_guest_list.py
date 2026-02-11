guest_list = ['Aaishwarya Ghuge', 'Harsh Pawar', 'Shivtej Thorat']
guest_list[-1] = 'Shivam Tarate'    #replaces last item in list
guest_list.insert(0, 'Parth Kulkarni')  #adds new item to the beginning of list
guest_list.insert(2, 'Pankaj Sakhre')   #adds new item to the 3rd position of list
guest_list.append('Vivek Jadav')        #adds new item to the end of list
print(f'\nNew guest list: {guest_list[0]}, {guest_list[1]}, {guest_list[2]}, {guest_list[3]}, {guest_list[-2]}, {guest_list[-1]}')
# Now shrinking the guest list to only two people
print('\nSorry guys, due to unavoidable circumstances, I can only invite two people for dinner.')
first_removed = guest_list.pop()
print(f"\nSorry {first_removed}, I can't invite you to dinner.")
print(f'\nYou are still invited, {guest_list[1]}, {guest_list[3]}')
#print(guest_list)
second_removed = guest_list.pop()
print(f"\nSorry {second_removed}, I can't invite you to dinner.")   
print(f'\nYou are still invited, {guest_list[1]}, {guest_list[3]}')
print(guest_list)
third_removed = guest_list.pop(0)
print(f"\nSorry {third_removed}, I can't invite you to dinner.")
#print(guest_list)
print(f'\nYou are still invited, {guest_list[0]}, {guest_list[2]}')
fourth_removed = guest_list.pop(1)
print(f"\nSorry {fourth_removed}, I can't invite you to dinner,")
print(guest_list)
print(f'\nYou are still invited, {guest_list[0]}, {guest_list[1]}')

del guest_list[1]
del guest_list[0]
print(f'\nFinal guest list: {guest_list}')