# python  bubble sort

'''

nums = [3,-1,0,10,8,6,2]

at iteration 1 

3 > -1 [-1,3,0,10,8,6,2]

3 > 0  [ -1, 0 , 3, 10, 8, 6, 2]

3 > 10 [ -1,  0 , 3, 10, 8, 6, 2]

10 > 8 [ -1 , 0 , 3, 8 , 10 , 6, 2 ]

10 > 6 [ - 1, 0 , 3, 8, 6, 10 , 2]

10 > 2 [ -1, 0 , 3, 8, 6, 2, 10]

at 2nd interation 

 -1 > 0 
 
 0 > 3 
 
 3 > 8 
 
 8 > 6 ==> [-1, 0 , 3, 6, 8, 2 , 10]
 
 8 > 2 ==> [-1, 0 , 3, 6 , 2, 8, 10]
 
at 3rd iteration

-1 > 0 

0 > 3 

3 > 6

6 > 2 ==> [-1,0, 3, 2, 6 , 8 , 10]

at 4th iteration

-1 > 0 

0 > 3 

3 > 2 ==> [-1, 0 , 2, 3, 6, 8, 10]



'''
# nums = [3,-1,0,10,8,6,2]


# for i in range(len(nums)-1):
    
#     for j in range(len(nums)-1 - i ):
        
#         if nums[j] > nums[j + 1]:
            
#             print(f"{nums[j]} > {nums[ j + 1] }")
            
#             nums[j] , nums[j + 1] = nums[j + 1] , nums[j]
            
#             print( f"so swap ==>{nums}")
# print(nums)


# Slicing 
#        0  1  2  3   4    5
# nums = [ 1, 2, 3, 4,  5,   6]

# #       -6,-5, -4 -3   -2   -1

# print(nums[0:5:2]) # here 0 is start and 5 is end & upper boundery is not 

# # considerable and 2 is step

# num = nums[:] # i f we are not gonna mention start, end, step it will copy 
# # entire list


# print(nums[::-1])

# print(nums[ -1: -4: -1])
# print(num)

# shallow copy and deep copy 
'''
when we assign a variable to the value of another variables they both 
will point to same adress beacause like example moving a file4

'''

# nums = [1,2,3,4,5]

# num = nums

# print(id(nums))
# print(id(num))

# num2 = nums[:]

# print(id(nums))
# print(id(num2))


# leetcode two sum problem

nums = [2,5,7,11]; target = 9

# for i in range(len(nums)):
    
#     for j in range(i + 1, len(nums)):
        
#         if nums[i] + nums[j] == target:
            
#             print(i , j )
#             break
            

'''
i = 0 ; j = 3
2 + 11  => 13 , j -= 1

i = 0 ; j = 2

2 + 7 = 9
'''

i = 0 ; j = len(nums) - 1

while i <= j :
    
    if nums[i] + nums[j] == target:
        
        print(i , j )
        
        break
    elif nums[i] + nums[j] > target:
        
        j -= 1
    else:
        
        i += 1

# selection sort

# -----------------------------
# Selection Sort
# -----------------------------

# List to sort
numbers = [64, 25, 12, 22, 11]

print("Before Sorting:", numbers)

# Go through each position in the list
for i in range(len(numbers) - 1):

    # Assume the current element is the smallest
    min_index = i

    # Check the remaining elements
    for j in range(i + 1, len(numbers)):

        # If a smaller number is found
        if numbers[j] < numbers[min_index]:
            min_index = j

    # Swap the current element with the smallest element
    numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

print("After Sorting :", numbers)


# -----------------------------
# Diamond Pattern
# -----------------------------

n = 5

print("\nDiamond Pattern:\n")

# Hollow Diamond Pattern

n = 5

# --------------------
# Upper Half
# --------------------
for i in range(n):

    # Print leading spaces
    print(" " * (n - i - 1), end="")

    # Print stars and spaces
    for j in range(2 * i + 1):

        # Print star at first or last position
        if j == 0 or j == 2 * i:
            print("*", end="")
        else:
            print(" ", end="")

    print()


# --------------------
# Lower Half
# --------------------
for i in range(n - 2, -1, -1):

    # Print leading spaces
    print(" " * (n - i - 1), end="")

    # Print stars and spaces
    for j in range(2 * i + 1):

        # Print star at first or last position
        if j == 0 or j == 2 * i:
            print("*", end="")
        else:
            print(" ", end="")

    print()
