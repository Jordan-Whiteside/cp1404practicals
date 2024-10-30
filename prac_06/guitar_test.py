"""Guitar test program."""
from prac_06.guitar import Guitar

gibsion = Guitar("Gibson L-5 CES", 1922, 16035.40)
another_guitar = Guitar("Another guitar", 2013, 100.0)


print(f"Gibson L-5 CES get_age() - Expected 102. Got {gibsion.get_age()}")
print(f"Another Guitar get_age() - Expected 11. Got {another_guitar.get_age()}")
print(f"Gibson L-5 CES is_vintage() - Expected True. Got {gibsion.is_vintage()}")
print(f"Another Guitar is_vintage() - Expected False. Got {another_guitar.is_vintage()}")