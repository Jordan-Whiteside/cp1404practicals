"""import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3"""

# What did you see on line 1?
# I saw any number between 5 and 20 inclusive
# 12, 11, 20, 10, 14

# What did you see on line 2?
# I saw any number between 3 and 10 exclusive
# 9, 5, 5, 3, 7

# What did you see on line 3?
# I saw any number between 2.5 and 4.5 including all decimal points up to 15 (Assuming that's PyCharms built in limit)
# 4.493337232785274, 4.845204523572509, 5.07702194382949, 3.2803101568278796, 5.108367549074288

import random # Assume this is the top of code
print(random.randrange(1, 10))