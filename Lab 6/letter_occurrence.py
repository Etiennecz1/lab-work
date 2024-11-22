# def letter_occurrence(input_string):
    # complete function implementation...
def letter_occurrence(input_string):
    # Initialize an empty dictionary to store the count of each letter
    letter_count = {}

    # Loop through each character in the string
    for char in input_string:
        # Convert character to lowercase to handle case insensitivity
        char = char.lower()
        
        # Check if the character is a letter (A-Z or a-z)
        if char.isalpha():
            # Increment the count of the letter in the dictionary
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1

    # Return the dictionary containing the letter counts
    return letter_count




 # return count
