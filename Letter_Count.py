import pprint

message =  \
'''
LOREM IPSUM GENERATOR
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna 
aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint 
occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
'''

letter_count = {}

for character in message:
    letter_count.setdefault(character, 0)
    letter_count[character] = letter_count[character] + 1

pprint.pprint(letter_count)