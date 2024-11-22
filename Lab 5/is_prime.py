def is_prime(num):
    """Checks if a number is prime.

    Input:
        num (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.

    Example:

    boolean = is_prime(5)   # returns True
    print(boolean)
    """


    # Function implementation here ...
def is_prime(num):
     if num <= 1:
        return False
     for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:  # If num is divisible by i, it's not prime
             return False
        return True  # If no divisors were found, it's prime 
     
print(is_prime(7))  # Output: True (7 is prime)
print(is_prime(10)) # Output: False (10 is not prime)
print(is_prime(11)) # Output: True (11 is prime)
print(is_prime(1))  # Output: False (1 is not prime) return output


# # # Run code example
# boolean = is_prime(5)   # returns True
# print(boolean)
  