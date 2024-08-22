# Ask user for their name. 
# Remove white spaces from string and Capitalize every word in a sentence
name = input("What's your name? ").strip().title()

# Split user's name into first name and last name 
first, last = name.split(" ")

# Say hello to the user's full name
print(f"hello, {name}")

# Say hello to the user's first name
print(f"Good Evening, {first}")

# Say hello to the user's last name
print(f"Good Morning, {last}")
