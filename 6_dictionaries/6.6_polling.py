favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

poll_candidate = ['sarah', 'edward', 'mike', 'loius']
for person in poll_candidate:
    if person in favorite_languages:
        print(f'Thank you {person.title()} for taking the poll.')
    else:
        print(f'{person.title()} please take the poll.')