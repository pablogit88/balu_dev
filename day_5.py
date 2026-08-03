# single line codes

# basic method

# intermidiate method

# advance method

'''

Amstrong number 

153 ==> it has length 3

do power with each of it's entire number length

1**3 + 5**3 + 3 **3 ==> 1 + 125 + 27 ==> 153 


'''

#basic method
# num = 153

# last_compare  = num

# temp = num


# power = 0 

# while num >0:
    
#     power += 1
    
#     num //= 10

# total = 0 

# while temp > 0:
    
#     digit = temp % 10
    
#     total += digit ** power
    
#     temp //= 10

# if last_compare == total:
    
#     print("Amstrong")
# else:
    
#     print("not")
    

# intermidiate

# num = 153 

# power = len(str(num))

# total = 0

# for  i in str(num):
    
#     print(i,type(i))
    
#     total += int(i) ** power

# print("amstrong" if total == num else "not")


#advanced method

# num = 153

# print("yes" if  num == sum([int(i) ** len(str(num)) for i in str(num)]) else "no")
    


# lists = [1,2,3,4]

# print(sum(lists))


'''

5! 

 5 * 4 * 3 * 2 * 1 ==> 120
 
sum of factorial of each number should equal to that number is called 

strong number


'''

# basic 

'''

145 

what we need

i need to extract each digit from the end

5! + 4! + 1! ==> 145

num % 10 ==> it is used to extract last digit

until we delete the last digit we cannot get 4 and 1 as well

for deleting we use num //= 10 ==> 145 //10 ==> 14 as a result 

if we get last digit 5 , now we need 5 factorial

take total as 1 

now run a loop until that number 5 

loop --> 1 to 5

1 * 1 ==> total = 1

2 * 1 ==> 2

3 * 2 ==> 6 

4 * 6 ==> 24

5 * 24 ==> 120 

'''
# Basic method of strong number 
# num = 145 

# total = 0

# temp = num

# while num > 0:
    
#     digit = num % 10
    
#     fact = 1
    
#     while digit >= 1:
        
#         fact *= digit
        
#         digit -= 1
        
#     total += fact
    
#     num //= 10
    
# print("yes" if temp == total else "no")

# intermidiate method

# num = 145 

# total = 0

# for i in str(num):
    
#     digit = int(i)
    
#     fact = 1
    
#     for j in range( 1, digit + 1) :
        
#         fact *= j
    
#     total += fact
    

# Advanced method

import math

num = 145

print("yes"  if num == sum([math.factorial(int(i))for i in str(num)]) else "no")



    
