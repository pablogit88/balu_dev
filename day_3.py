'''

* 
**
***
****
*****

it is not about programming , discussing about the midset we have to 

build the mind for problem solving.....

1 ==> i need stars to print

2 ==> i have 5 rows

3 ==> stars gettting increased at each step 

4 ==> each step a star is adding up

5 ==> i have 5 rows and for each row i need those many lines stars

6 ==> i need while loop and i need to iterate from 1 to 5 

7 ==> i need to print stars based on the i value

8 ==> i need inner loop to keep an eye on i value because i need stars 

        based on i value.





'''


# n = 5

# #outer loop

# i = 1 

# # while i <= 5: # i = 1 ; 2 <= 5; 3 <= 5 ; 4 <=5  ; 5 <= 5 , 6<= 5
    
# #     j = 1 
    
# #     while j <= i: # 1 <= 1 ; 2 <= 1 loop breaks here ; 1 <= 2; 2 <= 2
# #     # 3 <= 2 lopp breaks;  1 <= 3 ; 2<= 3 , 3 <= 3 ; 4 <= 3 lb; 
# #     # 1 <= 4 , 2 <= 4 , 3 <= 4 , 4 <= 4, 5 <= 4 lb
# #     # 1 <= 5 ; 2 <= 5 , 3<= 5 , 4<= 5 , 5<= 5, 6<= 5 lb
# #         print("*", end ="")
        
# #         j += 1 # j = 1+ 1  ; j = 3 
# #     print()
# #     i += 1 # i = 1+ 1 = 2; i = 3; i = 4 ; i = 5 ; i = 6


# while i <= 5:
    
#     print(i *"*")
    
#[print(' '*(n-1)+'*'*(2*i-1)) for i in range(n+1)] 


'''

code for equilateral trinagle





        *
      * * * 
    * * * * * 
  * * * * * * *
* * * * * * * * * 

i need 5 rows

first i need   1 single 2 * 1 - 1 => 1 ; i  need 4 ( n- 1) spaces  ;i = 1  

seciond i need 3 stars  2 * 2 - 1 ; i need  3   (n - 2)spaces ; i = 2  

third i need   5 stars  2* 3 - 1; i need  2   (n- 3) spaces   ; i = 3 

four i need    7 stars  2 * 4 -1 ; i need  1   ( n - 4) space    ;i = 4 

five  i need   9 stars 2 * 5 - 1 ; i need  0   ( n - 5) space     ;i = 5



'''
# n = 5
# i = 1

# while i<= 5:
    
#     print(" " * (n - i) + "*" * (( 2 * i) - 1))
    
#     i += 1



'''

1 
12 
123
1234
12345

i need 5 rows

i need 1 single  

i need 1 &  2

i need 1  , 2 , 3

i need 1, 2, 3 , 4 

i  need 1, 2, 3, 4 , 5


'''

# n = 5 

# i = 1

# while i <= 5: # 1 <= 5 ; 2 <= 5
    
    
#     j = 1 
    
#     while j <= i: #1 <= 1 2<= 1 lb; 1<= 2 ; 2<= 2 ; 3<= 2
        
#         print(j ,end = " ") # 1 ; 1 2
        
#         j += 1 # 2 3 
#     print()
#     i += 1 # 2


'''

A
AB
ABC
ABCD
ABCDE



'''
