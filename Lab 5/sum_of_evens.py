def sum_of_evens(min_value, max_value):
    
    """Find the sum of even numbers between two given numbers (inclusive).

    Args:
        min_value (int): Minimum number
        max_value (int): Maximum number

    Returns:
        total: sum of the even numbers between min_value and max_value

    Example:

    min_value = 10
    max_value = 13
    total = sum_of_evens(min_value, max_value)
    print(total) # total is 22.

    """



    # Function implementation here ...

def sum_of_evens(min_value, max_value):
    total_sum = 0  
    
    if min_value % 2 != 0:
        min_value += 1 
    for num in range(min_value, max_value + 1, 2):
        total_sum += num 
    return total_sum

result = sum_of_evens(10, 13)
print(result) 


# # # Run code example
# min_value = 10
# max_value = 13
# result = sum_of_evens(min_value, max_value) # returns 22
