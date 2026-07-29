# bitwise operators

a = 4

b = 3


'''

    1   0   0

    0   1   1
 &   
--------------------

    0              0        0 
   2 ** 2       2 ** 1     2 **0
   
   0   + 0 + 0 ==> 0 
   
4 ==>  2 ** 2 ,  1  0  0 


3 =>  0  1   1

5 ==> 1  0  1

6 ==> 1  1  0

7 ==> 1  1  1 
8 ==> 1  0  0  0 

9 ==> 1  0  0  1

10 ==> 1 0 1 0
   
 '''
print(4 & 3)


# OR | operator 

'''

 1   0   0 
 0   1   1
-----------
 1   1    1
 
 '''
print(4 | 3) 


# left shift << 

'''

4 << 1

 1   1   0 . 0 0  0  0 
 
 4 ==> 1 0  0  0 . 0 0  0  0 
output = 8


3 << 1

 0    1    1 . 0 0  0  0 
 
 3 ==> 0  1  1  0 . 0 0  0  0 
 
output = 6 


4 << 2 

1  0  0  0  0. 0 0 0 0 

output = 16



'''

# right shift 

'''

1 0 0 ==> 4

4 >> 2

 1  . 0 0 0 
 
 output = 1
'''

# Decision making statements

'''

if 

if else

if elif else

nested if

'''

a = 10 

if a > 0:
    
    if a % 2 == 0:
        
        print("positive and even ")
    else:
        
        print("Negative and odd")

    


# logical operators  and or not

if a > 0 and a % 2 ==0:
    
    print("positive and even")
else:
    print("positive and odd")


# or operator 

if a > 0 or a % 2 ==1:
    
    print("positive and odd")
else:
    print("positve  and even")
    
# not operator

state = False

if not state:
    
    print("yes")
else:
    
    print("no")
#--------------------------------------------------------------------

# shorthand methods

num = 10

print("yes" if num % 2 == 0 else "no")

# i  = 1

# while i <= num:
    
#     print("balu")
    
#     i += 1
    
for  i in range(num):
    
    print("balu")
    
nums = [1,2,3]

for i in nums:
    
    print(i)

for i in range(len(nums)):
    
    print(i)

# when you need index along with numbers so we use enumerate

for ind, element in enumerate(nums):
    
    print(ind,element)
    
nums = [1,2,3,4,5,6,7,8,9,10]

for i in nums:
    
    if i % 2 ==0:
        
        print(i)
print(*[i for i in nums if i % 2 ==0])


for i in nums:
    
    if i % 2 ==0:
        
        print(i , "even")
    else:
        print(i , "odd")
# Comprehension methods 
        
print(*[(i, "even") if i % 2 ==0 else (i , "odd") for i in nums])





