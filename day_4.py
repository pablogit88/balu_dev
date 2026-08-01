# even number check
'''
num & 1 ==0

num = 5 

 1  0   1
&       1
-------------
  0  0   1

num = 6 

  1   1   0
& 0   0   1
--------------
  0   0    0 ==> 0 
  
 '''
 
# for i in range(1, 11):
     
#     if  not i & 1 :
        
#         print(i)
#print(*[i for i in range(2,11) if not i & 1 ] ,sep = "\n")


# data structures

'''

List -> stores large amount of different types of data at one place

and it is mutable , mutable in the sense we can add values, remove, 

modify the existing values .


'''


# lists  = [1,2,3,4,5,6,7,8,9,10,2,]

# lists.append(11)

# print(lists)

# lists.pop()

# lists.remove(1)



# lists.insert(0, 1)

# lists.count(1)

# second_list = lists.copy()

# second_list.sort()

# lists.reverse()

# lists.pop(1)



# count = 0 
# for i in lists:
    
#     if i == 2:
        
#         count += 1
# print(count)

# print(lists.index(2))


# cnt = 0 

# for ind,ele in enumerate(lists):
    
#     if ele == 2:
        
#         index = i
        
#         cnt += 1
#     if cnt > 1:
        
#         print(ind)
        
#         break
    
    
# print(max(lists))

# print(min(lists))

# print(len(lists))


nums = [1,2,3,4,5,6,7,8,9,9]

min_num = nums[0]

for i in nums[1:]:
    
    if i < min_num:
        
        
        min_num = i
print(min_num)

tuples = (1,2,3,4,"strings")

for i in tuples:
    
    print(i)
    
#
