def reverse_array(arr):
    arr.reverse()
    return arr 


arr1 = [1, 2, 3, 4, 5]
reverse_array(arr1)
print(arr1)  # Output: [5, 4, 3, 2, 1]

print(" ".join(map(str, arr1)))

# time complexity: O(n) - linear- each element is visited once
# space complexity: O(1) as no extra space is used
