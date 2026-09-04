def paneCheppadu(n:int) -> None:
    
    if n % 2 == 0:
        
        return True
    else:
        return False
        
        
n = int(input())
chesa = paneCheppadu(n)

rendo_sare = paneCheppadu(n)

print(chesa)
    
print(rendo_sare)

'''

****Arguments****

postional arguments

default 

list of arguments

keyword 

list of keyword
'''

# postional 
def addition(a, b): # arguments
    
    return a + b

print(addition(2,3)) # parameters

# default 
def addition( a = 3 , b = 5):
    
    return a + b

print(addition())

# lsit of arguments

def args(*balu):
    
    return sum(balu)

print(args(1,2,3,4,5,6,7,8,9))


# keyword arguments

def kargs(a ,b ):
    
    return a + b

print(kargs(b = 5 , a = 3))

#List of Keyword arguements

def listOfKargs(**prints):
    
    return prints

print(listOfKargs(a = 2 , b = 3 , c = 5 , d = 8 ))
    




    
