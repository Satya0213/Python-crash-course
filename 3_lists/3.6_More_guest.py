guest_list = ['Aaishwarya Ghuge', 'Harsh Pawar', 'Shivtej Thorat']
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

#efficient way
guests = ["Albert Einstein", "Cleopatra", "Nikola Tesla", "Marie Curie"]
print("Great news! We found a bigger table, so we can invite more guests!\n")

# Add to the beginning
guests.insert(0, "Isaac Newton")

# Add to the middle
middle = len(guests) // 2
guests.insert(middle, "Ada Lovelace")

# Add to the end
guests.append("Charles Darwin")

print("--- Updated Invitations ---\n")
for guest in guests:
    print(f"Dear {guest}, I would be honored if you joined me for dinner this Saturday evening. Hope to see you there!")