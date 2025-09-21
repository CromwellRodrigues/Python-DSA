# find the minimum and maximum value in the array using minimum number of comparisons. 

def set_min(arr) :
    # initialise mini as a positive infinity
    min = float('inf')  
    
    for num in arr:
        if num < min:
            min = num
    return min

def set_max(arr) :
    # initialise maxi as a negative infinity
    max = float('-inf')  
    
    for num in arr:
        if num > max:
            max = num
    return max

# Driver code
arr1 = [ 4, 8, 3, 2, 1, 7 ]

print("Minimum value : ", set_min(arr1)) # 1
print("Maximum value : ", set_max(arr1)) # 8


# Time complexity: O(n) - each element is visited once
# Space complexity: O(1) - only a fixed amount of extra space is used