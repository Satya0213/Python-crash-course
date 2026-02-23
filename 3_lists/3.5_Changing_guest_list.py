#Changing Guest List: You just heard that one of your guests can’t make the 
#dinner, so you need to send out a new set of invitations. You’ll have to think of 
#someone else to invite.
#• Start with your program from Exercise 3-4. Add a print() call at the end of 
#your program, stating the name of the guest who can’t make it.
#• Modify your list, replacing the name of the guest who can’t make it with the 
#name of the new person you are inviting.
#• Print a second set of invitation messages, one for each person who is still in 
#your list.

print('--method 1--')
guest_list = ['Aaishwarya Ghuge', 'Harsh Pawar', 'Shivtej Thorat']
print(f"\nHey {guest_list[0]}, \nLets have dinner together soon! can't wait to catch up.")
print(f"\nHey {guest_list[1]}, \nLets have dinner together soon! can't wait to catch up.")
print(f"\nHey {guest_list[2]}, \nLets have dinner together soon! can't wait to catch up.")

not_coming = guest_list.pop(-1)     #removes last item from list and returns it
print(f"\nUnfortunately, {not_coming} can't make it to dinner.")
guest_list.append('Shivam Tarate')  #adds new item to the end of list
print(f"\nHey {guest_list[0]}, \nLets have dinner together soon! can't wait to catch up.")
print(f"\nHey {guest_list[1]}, \nLets have dinner together soon! can't wait to catch up.")
print(f"\nHey {guest_list[2]}, \nLets have dinner together soon! can't wait to catch up.")

#method 2
print("\n---method 2---")
guest_list = ['Aaishwarya Ghuge', 'Harsh Pawar', 'Shivtej Thorat']
print(f"\nHey {guest_list[0]}, \nLets have dinner together soon! can't wait to catch up.")
print(f"\nHey {guest_list[1]}, \nLets have dinner together soon! can't wait to catch up.")
print(f"\nHey {guest_list[2]}, \nLets have dinner together soon! can't wait to catch up.")

print(f"\nUnfortunately, {guest_list[-1]} can't make it to dinner.")
guest_list[-1] = 'Shivam Tarate'    #replaces last item in list
print(f"\nHey {guest_list[0]}, \nLets have dinner together soon! can't wait to catch up.")
print(f"\nHey {guest_list[1]}, \nLets have dinner together soon! can't wait to catch up.")
print(f"\nHey {guest_list[2]}, \nLets have dinner together soon! can't wait to catch up.")

#efficient way
guests = ["Albert Einstein", "Cleopatra", "Leonardo da Vinci", "Marie Curie"]

print("--- First Invitations ---\n")
for guest in guests:
    print(f"Dear {guest}, I would be honored if you joined me for dinner this Saturday evening. Hope to see you there!")

# Exercise 3-5: Changing Guest List
print("\n--- Guest Change Notice ---\n")

cancelled_guest = "Leonardo da Vinci"
print(f"Unfortunately, {cancelled_guest} is unable to attend dinner.")

# Replace the guest who can't make it
new_guest = "Nikola Tesla"
guests[guests.index(cancelled_guest)] = new_guest

print(f"\n{new_guest} has been invited in their place!")

print("\n--- Updated Invitations ---\n")
for guest in guests:
    print(f"Dear {guest}, I would be honored if you joined me for dinner this Saturday evening. Hope to see you there!")