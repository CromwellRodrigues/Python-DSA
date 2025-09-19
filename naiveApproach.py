# naive approach using a temporary array
# create a temporary array of the same size as the original array 
# copy elements from the original array to the temporary array in reverse order
# copy elements from the temporary array back to the original array

def reverse_array(arr): 
    n = len(arr) 
    print("length of array:", n)

    # temporary array to store reversed array
    temp = [0] * n
    
    # copy elements from original array to temporary array in reverse order
    for i in range(n):
        temp[i] = arr[n-i-1]
      
        
    # copy elements from temporary array back to original array
    for i in range(n):
        arr[i] = temp[i]
        
arr1 = [1, 2, 3, 4, 5]
reverse_array(arr1)
print(arr1)  # Output: [5, 4, 3, 2, 1]


arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
reverse_array(arr2)
print(arr2) 

# time complexity: O(n)
# space complexity: O(n) due to the temporary array to store the reversed elements

# Note: This approach is not optimal in terms of space complexity.