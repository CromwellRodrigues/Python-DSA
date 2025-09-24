# given a number N. find if the digit sum (sum of all digits) of N is a palindrome or not. 

def is_palindrome(N):
    
    digit_sum = 0
    
    temp = N 
    
    while (temp  > 0):
        digit_sum += temp % 10 
        temp //= 10
        
    # reverse the digit sum 
    rev = 0 
    temp = digit_sum  
    
    while (temp > 0):
        rev = rev * 10 + (temp % 10)
        temp //= 10
        
    return 1 if digit_sum == rev else 0 
        
print(is_palindrome(1239))  # 15
print(is_palindrome(9292))  # 22
