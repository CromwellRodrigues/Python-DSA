# swap elements in an array

def reverse_array(arr):
    n = len(arr) 
    
    for i in range(n//2): 
        temp = arr[i]
        arr[i] = arr[n-i-1]
        arr[n-i-1] = temp
        
        
arr1 = [1, 2, 3, 4, 5,6,7,8,9,]
reverse_array(arr1)
print(arr1)  # Output: [5, 4, 3, 2, 1]


# time complexity: O(n) the loop runs n/2 times
# space complexity: O(1) no extra space is used