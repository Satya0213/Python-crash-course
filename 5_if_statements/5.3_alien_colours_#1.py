#passes if statemen
alien_colour = 'green'
if alien_colour == 'green':
    print('Player earned 5 points.')

#does not pass if statement
alien_colour = 'red'
if alien_colour == 'green':
    print('\nPlayer earned 5 points.')
else:
    print('\nPlayer did not earn any point')