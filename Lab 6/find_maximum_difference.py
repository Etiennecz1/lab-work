# def find_maximum_difference(a, b):
#     # code implementation here...
def find_maximum_difference(a, b):
    max_diff = 0
    for num_a in a:
        for num_b in b:
            diff = abs(num_a - num_b)
            if diff > max_diff:
                max_diff = diff
                
    return max_diff

a = [1, 3, 7, 9]
b = [2, 5, 6]
result = find_maximum_difference(a, b)
print(f"The maximum difference between lists a and b is: {result}")


#     return maximum



