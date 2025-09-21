# divide the array into two parts and compare the maximums and minimums of the two parts to get the max and min of the whole array 

# low - index of the first element of the subarray - left (start)
# high - index of the last element of the subarray - right (end)

def getMinMax (low, high, arr):
    arr_min = arr[low] 
    arr_max = arr[high]  
 
     
    
    # If there is only one element
    if low == high :
        arr_min = arr[low]
        arr_max = arr[low]
        
        return (arr_min, arr_max)
    
    
    # if there are two elements 
    elif high == low + 1 :
        if arr[low] > arr[high] :
            arr_min = arr[high]
            arr_max = arr[low]
            
        else :
            arr_min = arr[low]
            arr_max = arr[high]
           
        return (arr_min, arr_max)
    
    else : 

        # if there are more than two elements
        mid = int(low + high) // 2
        arr_min1, arr_max1 = getMinMax(low, mid, arr)
        arr_min2, arr_max2 = getMinMax(mid + 1, high, arr)
        
    return(min(arr_min1, arr_min2), max(arr_max1, arr_max2))


arr1 = [100, 22, 485, 10, 309, 995]

high = len(arr1) - 1 
low = 0 

arr_min, arr_max = getMinMax(low, high, arr1)

print("Minimum:", arr_min) # 1
print("Maximum:", arr_max) # 992

# Time complexity: O(n) - each element is visited once
# Space complexity: O(log n) - due to recursive stack space, meaning the space used grows logarithmically with input size, the stack space will be filled for the maximum height of the tree formed during recursive calls same as binary tree