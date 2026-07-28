#python is nothing but english

# variables
name_of_user = "Balu" # snake case

'''
should not intiate with numbers and operators

Data types:

      int --> 1,2,3

      float --> 1.2,

      string -> 'balu' , 'b' , "balu"

      boolean -> true, false
     
      complex -> 3 + 2j

      id is nothing but adsress

      type casting

      
      
'''

annaya_chethelo = "matakasra"

thammudu_chethelo = "matakasra"

print(id(annaya_chethelo))

print(id(thammudu_chethelo))




print(type(10))


a = 10

a = 10.256788990000

b = int(a)

print(type(a))

print(type(b))

print(b)

c  = 20

d = float(c)

print(type(c))

print(type(d))

print(d)


e = 100

f = str(e)

print(type(e))

print(type(f))

print(f)


g = int(f)

print(g)


h = "balu"

# Ascii values

print(ord("b"))
print(ord("q"))
print(ord("l"))
print(ord("u"))

print(ord("b")+ ord("a") + ord("l") + ord("u"))

print(chr(98))


''' 

from 65 -96 A-Z
97 -122 a -z 

'''
# arthemetic

# relational & comparison are both same

# assignment

# identity

# membership

#bitwise

# logical operators it is interlinked with decisoion making statements

'''

+ , - , / , // , % 

> , < , <= , >= , != , ==

a = 10

a  = a + 1

a += 1

+= , -= , *= , /= , %= 

is , is not 

in , not in

& , | , >> , << , ~ 

and,  or  , not


'''

# a = 10/ 3

# print(a)

# b = 10 // 3

# print(b)


# relational operators

# print( 10 < 20)

# print(10 > 20)

# print(20 <= 20)

# print(20 >= 20)

# print(10 != 20)

# print(10 == 10)


# assignment

# a = 20

# a += 10

# a *= 200

# a /= 10

# a //= 10

# a %= 2

# print(a)

# # identity operator 

# annaya = "good guy"

# thammi = "bad guy"


# print(annaya is thammi)

rak = ['a', 'b','c']

rak_slice = rak[:]

print(rak is rak_slice)

'''

rak has a option to add books

is is going to check the adress not the values blindly


is there any same value stored in different variables they will 

both located to same address

rak_slice has a option to add more books

books added and adress got changed 

hence both are not located to same address to we will get false

because of "is" operator


== is used for comparing values only

but is going to check values with address


Ex: fish we used 



'''

print(rak is rak_slice)

print(rak == rak_slice)




# memebership 

print( 'a' in rak)

print('d' not in rak)







