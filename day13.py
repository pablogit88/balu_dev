# # today topic is about the scopes we have in python

# '''

# 1. Global Scope

# 2. Local Scope 

# 3. Non - Local Scope

# 4. Built In scope # print, max  , min , 

# '''

# # Global Scope

# x = 10 

# def globalScopeExplaining() -> int:
    
#     global x
    
#     x = 20
    
#     return x
# print(globalScopeExplaining())


# # Local scope 

# def outer():
    
#     x = 20
    
#     return x + 10

# print(outer())


# # Non - local scope

# def outer():
    
#     x = 20
    
#     def inner():
        
#         nonlocal  x 
        
#         #x = 40
        
#         return x
#     return inner()

# print(outer())

# Recurrsion

'''
tail recurssion

liner recurrsion

when we have large number of input we break it into chunks until we got

small input from there we will calculate

'''
# sum of 1 to n numbers ( for example n = 5) this is linear recurrsion

# def sumup(n):
    
    
#     if n <= 0:
        
#         return 0
#     return n + sumup(n - 1)

# print(sumup(5))


# tail recurrsion

# def sump(n, c = 0):
    
#     if n <= 0:
        
#         return 0
        
#     return n + sump(n - 1, c + n)

# print(sump(5))


# def feb(n):
    
#     if n <= 1:
        
#         return n
#     return feb(n - 1) + feb( n - 2)
    
# print(feb(6))
    
