# Demonstrates import and random.choice

# NB: When you use `import random`, you can now have a userdefined function named choice since pythonallows you to scope the names

import random

coin = random.choice(["heads", "tails"])
print(coin)