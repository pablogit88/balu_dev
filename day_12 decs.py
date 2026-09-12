# decorators

'''

it detects the type of data during the run time.

'''
# this is normal decorator

def outer(func): 
    
    def inner():
        
        scan = func() 
        
        print(f'{scan} is output of original function')
        
        '''
        
        here parent is outer function which takes the input 
        
        of original function that we like to process without 
        
        modifying the original function. 
        
        so inner function carries the output of original function which i
        
        is [1,2,3,4,5,6,7,8] and we are returning it with sum(scan)
        
        which is sum([1,2,3,4,5,6,7,8])  this is output of inner.
        
        '''
        return  sum(scan)//sum(n)
    return inner
@outer([1,2,3,4])
def decorators()-> list[int]:
    
    return [1,2,3,4,5,6,7,8]

# @outer
# def second_dec():
    
#     return [10,11,12,13,14,15,16]
    
print(decorators)
#print(second_dec)

# ----------------------------------------------------------------------------------------------------------------
# decorators

'''

it detects the type of data during the run time.

'''

# this decorator taking the parameter itself
def outer(n): # [1,2,3,4]
    
    def inner(func): # decorator
        
        scan = func() #[1,2,3,4,5,6,7,8]
        
        print(f'{scan} is output of original function')
        
        '''
        
        here parent is outer function which takes the input 
        
        of original function that we like to process without 
        
        modifying the original function. 
        
        so inner function carries the output of original function which i
        
        is [1,2,3,4,5,6,7,8] and we are returning it with sum(scan)
        
        which is sum([1,2,3,4,5,6,7,8])  this is output of inner.
        
        '''
        return  sum(scan)//sum(n)
    return inner
@outer([1,2,3,4])
def decorators()-> list[int]:
    
    return [1,2,3,4,5,6,7,8]

# @outer
# def second_dec():
    
#     return [10,11,12,13,14,15,16]
    
print(decorators)
#print(second_dec)

# ------------------------------------------------------------------------------------------------------------------
# decorators

'''

it detects the type of data during the run time.

'''

# this is about taking the dynamic input
def outer(func): 

    def inner(*args,**kwargs):
        
        scan = func(*args,**kwargs) 
        
        print(f'{scan} is output of original function')
        
        '''
        
        here parent is outer function which takes the input 
        
        of original function that we like to process without 
        
        modifying the original function. 
        
        so inner function carries the output of original function which i
        
        is [1,2,3,4,5,6,7,8] and we are returning it with sum(scan)
        
        which is sum([1,2,3,4,5,6,7,8])  this is output of inner.
        
        '''
        return  sum(scan)
    return inner
# with input in orginal function

@outer
def decorators(a:list[int],b:list[int])-> list[int]:
    
    a.extend(b)
    
    return a # [1,2,3,4,5,6,7,8])
    

a = list(map(int,input().split()))# we are supposed to take input as list

b = list(map(int,input().split()))

print(decorators(a,b))

# -----------------------------------------------------------------------------------------------------------------

# decorators

'''

it detects the type of data during the run time.

'''

#  this is about chain of decorators
def outer1(func): 

    def inner(*args,**kwargs):
        
        scan = func(*args,**kwargs) 
        
        print(f'{scan} is output of original function')
        
        '''
        
        here parent is outer function which takes the input 
        
        of original function that we like to process without 
        
        modifying the original function. 
        
        so inner function carries the output of original function which i
        
        is [1,2,3,4,5,6,7,8] and we are returning it with sum(scan)
        
        which is sum([1,2,3,4,5,6,7,8])  this is output of inner.
        
        '''
        return  [i for i in scan if i & 1 ==0]
    return inner
# output of outer func will be input to this
def outer2(func):
    
    def inner(*args,**kwargs):
        
        scans = func(*args,**kwargs)
        
        return sum(scans)
    return inner

@outer2
@outer1
def decorators(a:list[int],b:list[int])-> list[int]:
    
    a.extend(b)
    
    return a # [1,2,3,4,5,6,7,8])
    

a = list(map(int,input().split()))# we are supposed to take input as list

b = list(map(int,input().split()))

print(decorators(a,b))

