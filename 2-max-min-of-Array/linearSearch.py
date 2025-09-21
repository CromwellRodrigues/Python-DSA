# maximum and minimum of an array using linear search  

# initialise values of min and max of the first two elements.  

# the 3rd element will be compared with the min and max 

# class to store the minimum and maximum values found in the array
class Pair : 
    def __call__(self) : 
        self.min = 0
        self.max = 0
        

# takes the array and its length and creates a pair object called minmax to store the result
def getMinMax(arr: list, n: int) -> Pair : 
    minmax = Pair() 
    
    # if there is only one element 
    if n == 1 :
        minmax.max = arr[0]
        minmax.min = arr[0]
        return minmax
    
    # if there are more than one element
    if arr[0] > arr[1] : 
        minmax.max = arr[0]
        minmax.min = arr[1]
    else : 
        minmax.max = arr[1]
        minmax.min = arr[0] 
    
    
    for i in range(2, n) :
        if arr[i] > minmax.max : 
            minmax.max = arr[i]
        elif arr[i] < minmax.min : 
            minmax.min = arr[i]
            
    return minmax

arr1 = [100, 22, 485, 1, 309, 992]

minmax= getMinMax(arr1, len(arr1))

print("Minimum element is :", minmax.min) # 1
print("Maximum element is :", minmax.max) # 992

# Time complexity: O(n) - each element is visited once
# Space complexity: O(1) - only a fixed amount of extra space is used
# total number of comparisons is 1 + 2*(n-2) in worst case (descending order)  & 1 + (n-2) in best case (ascending order)

# this code efficiently find the minimum and max values in a single pass through the array using a helper class to store the results.rd /s /q "1-array Reverse\.git"
rd /s /q "2-max-min-of-Array\.git"