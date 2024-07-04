import re

def extract_letters_after_numbers(input_string):
    # Remove all spaces from the string
    input_string = input_string.replace(" ", "")
    
    # Use regular expressions to find all letters that follow a digit
    matches = re.findall(r'\d([a-zA-Z])', input_string)
    
    # Output each matched letter line by line
    for letter in matches:
        print(letter)

# Example usage
input_string = "1B 2C 3A 4D 5A 6A 7D 8D 9D 10 B 11 B 12 D 13 B 14 D 15 A 16 B 17 B 18 A 19 B 20 A 21 C 22 D 23 B 24 C 25 C 26 A 27 B 28 D 29 D 30 A 31 B 32 B 33 C 34 C 35 A 36 B 37 A 38 D 39 D 40 D"
extract_letters_after_numbers(input_string)
