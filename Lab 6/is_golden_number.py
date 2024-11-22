# def is_golden_number(n):
#     # function implementation ...
def is_golden_number(n):
    
    golden_ratio = 1.618033988749895
    
    if n > 1:
        ratio = n / (n - 1)
        tolerance = 0.01  
        if abs(ratio - golden_ratio) <= tolerance:
            return True
    return False

n = 2
result = is_golden_number(n)
print(f"Is {n} a golden number? {result}")

#     return boolean