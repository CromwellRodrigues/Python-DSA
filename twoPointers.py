# two pointers approach
# use two pointers, one starting at the beginning of the array and the other at the end
def reverse_array(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        # swap elements at left and right pointers
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr
arr1 = [1, 2, 3, 4, 5]
reverse_array(arr1)
print(arr1)  # Output: [5, 4, 3, 2, 1]


for i in range(len(arr1)):
    print(arr1[i], end=" ")  # Output: 5 4 3 2 1
    

# time complexity: O(n) - each element is visited once 
# space complexity: O(1) as no extra space is used