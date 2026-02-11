locations_to_visit = ['Udaipur', 'Goa', 'Manali', 'Shimla', 'Mahabalwshwar']
print("Original list:")
print(locations_to_visit)
print("\nSorted list:\n ",sorted(locations_to_visit)) #prints sorted list without changing original list
print("\nOriginal list again:\n",locations_to_visit) #original list remains unchanged
print("\nReverse list:")    
print(sorted(locations_to_visit, reverse=True))     #prints reversed sorted list
print("\nOriginal list again:\n",locations_to_visit)
print("\nReverse list:")
locations_to_visit.reverse()    #reverses the original list
print(locations_to_visit)  
print("\nOriginal list again:")
locations_to_visit.reverse()    
print(locations_to_visit)  
print('\nSorted list:')
locations_to_visit.sort()
print(locations_to_visit)   #sorts the original list permanently
print('\nReverse sorted list:')
locations_to_visit.sort(reverse=True)
print(locations_to_visit)   #sorts the original list in reverse order permanently



