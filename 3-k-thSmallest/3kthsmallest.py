# kth smallest element in an unsorted array 

import random



# partition function - rearrange elements around a pivot(the last element)
# low = starting index(0), high = ending index
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    # iterate through the subarray
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# randomized partition to improve performance on average, avoid worst-case scenarios
def randomPartition(arr, low, high):
    rand_index = random.randint(low, high)
    arr[rand_index], arr[high] = arr[high], arr[rand_index]
    return partition(arr, low, high)



# function to find the k-th smallest element using quickselect 
def quickselect(arr, low, high, k):
    if low <= high:
        pivot_index = randomPartition(arr, low, high)

        if pivot_index == k:
            return arr[pivot_index]
        elif pivot_index < k:
            return quickselect(arr, pivot_index + 1, high, k)
        else:
            return quickselect(arr, low, pivot_index - 1, k)
    return None



def kth_smallest(arr, k):
    return quickselect(arr, 0, len(arr) - 1, k - 1)


array1 = [7, 10, 24, 3, 20, 15] 
k = 4
array2 = [8, 39, 39, 94, 12, 7, 85]
print(kth_smallest(array1, k))  
print(kth_smallest(array2, 3))


# Time complexity: O(n) on average, O(n^2) in the worst case
# Space complexity: O(1) - in-place algorithm  O(log n) due to recursion stack, O(n) in worst case
