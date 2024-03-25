from random import choice , randint , shuffle

# Function to random choice between this two options
coin = choice(['heads', 'tails'])

# Function to choice a number between a range
number_random = randint(1,10)

# Function to just make a random order
cards = ['jack', 'queen', 'king']
unorder_cards = shuffle(cards)
for card in cards:
    print(card)
