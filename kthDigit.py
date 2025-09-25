# given two numbers A,B, find the k-th digit from the right of A^B  
 



def kth_digit(A, B, k):
    # Calculate A^B
    power_value = pow(A, B) 
    # Convert the result to string to easily access digits
    power_str = str(power_value)
    print(power_str)
    
    # Check if k is within the length of the string
    if k <= len(power_str):
        # Return the k-th digit from the right (1-based index)
        return int(power_str[-k])
    else:
        # If k is larger than the number of digits, return -1 or some indication
        return -1
    
    
    
print(kth_digit(23, 5, 4))  
print(kth_digit(14, 4, 3))  