Sum the Array
def sum_array(arr):

    if len(arr) == 0:
        return 0

    return arr[0] + sum_array(arr[1:])


print("--- Sum Tests ---")
print(sum_array([]))                
print(sum_array([5]))                 
print(sum_array([1, 2, 3, 4, 5]))      
print(sum_array([10, -5, 3, -2])) 


#Find the Largest Number
def find_max(arr):

    if len(arr) == 0:
        raise ValueError("Array must contain at least one number.")
    

    if len(arr) == 1:
        return arr[0]
    

    max_of_rest = find_max(arr[1:])
    if arr[0] > max_of_rest:
        return arr[0]
    else:
        return max_of_rest


print("\n--- Find Max Tests ---")
print(find_max([42]))
print(find_max([10, 5, 2, 1]))
print(find_max([1, 5, 2, 10]))
print(find_max([-5, -2, -10, -8]))
try:
    find_max([])
except ValueError as e:
    print(f"Empty array test: {e}")

#Find the Largest Number
def count_target(arr, target):

    if len(arr) == 0:
        return 0
    

    if arr[0] == target:
        match = 1
    else:
        match = 0
        

    return match + count_target(arr[1:], target)

print("\n--- Count Target Tests ---")
print(count_target([], 5))
print(count_target([1, 2, 3, 2, 4, 2], 2))
print(count_target([1, 2, 3, 4, 5], 9))
Compose
Write