guest_list = ['Rutuja Shinde', 'Harsh Pawar', 'Shivtej Thorat']
print(f'\nOld guest list: {guest_list[0]}, {guest_list[1]}, {guest_list[2]}')
print(f"\nUnfortunately, {guest_list[-1]} can't make it to dinner.")

guest_list[-1] = 'Shivam Tarate'    #replaces last item in list
print(f"\nHey {guest_list[0]}, {guest_list[1]}, {guest_list[2]}, I just found a bigger dinner table so more guests are invited! ")
guest_list.insert(0, 'Parth Kulkarni')  #adds new item to the beginning of list
guest_list.insert(2, 'Pankaj Sakhre')   #adds new item to the 3rd position of list
guest_list.append('Vivek Jadav')        #adds new item to the end of list
print(f"\nHey {guest_list[0]}, \nLets have dinner together soon! can't wait to catch up.")
print(f"\nHey {guest_list[1]}, \nLets have dinner together soon! can't wait to catch up.")
print(f"\nHey {guest_list[2]}, \nLets have dinner together soon! can't wait to catch up.")
print(f"\nHey {guest_list[3]}, \nLets have dinner together soon! can't wait to catch up.")
print(f"\nHey {guest_list[-2]}, \nLets have dinner together soon! can't wait to catch up.")
print(f"\nHey {guest_list[-1]}, \nLets have dinner together soon! can't wait to catch up.")