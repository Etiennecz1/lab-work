def winning_numbers(user_list, winning_list):
    """
    This function checks if the user's numbers match the predefined winning numbers.

    Parameters:
    user_list (list): A list of three integers representing the user's chosen numbers.
    winning_list (list): A list of integers representing the winning numbers.

    Returns:
    str: A string indicating the prize won:
        - "First" if all three numbers match the winning numbers.
        - "Second" if two numbers match the winning numbers.
        - "Third" if one number matches the winning numbers.
        - "No" if none of the numbers match the winning numbers.

    Example:
    --------
    winning_list = [5, 14, 17]
    user_list = [3, 5, 10]
    result = winning_numbers(user_list, winning_list)
    # Output: "Third" (since one number, 5, matches the winning numbers)

    user_list = [14, 5, 10]
    result = winning_numbers(user_list, winning_list)
    # Output: "Third" (since two numbers, 14 and 5, match the winning numbers)

    The function also prints a message indicating the prize won.
    """

    # Function implementation here ...
 
def check_winning_list(user_list, winning_list):
    correct_numbers = set(user_list) & set(winning_list)
    num_matches = len(correct_numbers)
    if num_matches == 1:
        return "Third"  
    elif num_matches == 2:
        return "Second"  
    elif num_matches == 3:
        return "First"  
    else:
        return "No match" 

user_list = [6, 5, 10]
winning_list = [3, 5, 10]
result = check_winning_list(user_list, winning_list)
print(result) 
 # Print the result
