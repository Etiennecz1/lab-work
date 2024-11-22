def calculate_average(numbers):
    """
    This function calculates the average of a list of numbers using a for loop.

    Parameters:
    ----------
    numbers : list
        A list of numerical values (int or float).

    Returns:
    -------
    float:
        The average of the numbers in the list. If the list is empty, returns None.

    Example:
    --------
    calculate_average([10, 20, 30, 40, 50])  # Output: 30.0
    """
    
    # Function implementation here ...
    def calculate_average(numbers):
        if len(numbers) == 0:
            return 0  
    total = sum(numbers)  
    count = len(numbers)
    average = total / count  
    return average 
numbers = [3, 7, 10, 12, 14, 18]
avg = calculate_average(numbers)
print("The average is:", avg) 


# # Example usage
# numbers = [10, 20, 30, 40, 50]
# print("The average is:", calculate_average(numbers))  # Expected output: The average is: 30.0
