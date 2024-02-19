# Collision Handling
# If we know keys in advance, then we can do "perfect Hashing". // so no collison happen here and it is useful to building from known things/keys. like making dictionary of known english words.


# Birthday Paradox
# If there are 23 people in a room then there is a probability of half value, that two people have the same birthday. means 50 % probability
# If people are 70 then this chances are go up to 90.99 % probability

# If we do not know keys, then we use one of the "following". // so collisoin are bound to happen
# 1. Chaining - Make a chain of colliding items
# 2. Open Addressing - we use same array, if position is occupied then we try to put it into another slot // not use chains 
#     a. Linear Probing
#     b. Quadratic Probing 
#     c. Double Hashing

# # watch GATE SMASHERS videos for understading concepts