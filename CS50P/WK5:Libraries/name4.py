# Demonstrates list slice

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

# sys.argv[1:] - Access arguments from index 1 uto the end of the list
for arg in sys.argv[1:]:
    print("hello, my name is", arg) 
