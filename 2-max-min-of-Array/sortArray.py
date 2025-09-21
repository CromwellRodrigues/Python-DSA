# first sort the array and then return the first and last element

def getMinMax(arr): 
    
    arr.sort() 
    minmax= {"Min": arr[0], "Max": arr[-1]}
    return minmax


arr = [100, 11, 329, 20, -10, 5, 0]
print(getMinMax(arr))


# Time complexity: O(n log n) - due to the sorting step, elements are visited /moved/ swapped multiple times, before reaching their final position
# Space complexity: O(1) - only a fixed amount of extra space is used