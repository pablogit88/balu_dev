# Dictonary 

'''

stores the data in key value pairs 

key should be unique  , value can be duplicate

{"roll_no" : 1 , "marks" : 98} 

we can create dictonary in three ways 

dictonary  = {"roll_no" : 1 , "marks" : 98} 

dicts = {}

dictsss = dict()


'''


student = {
    "name": "Rahul",
    "age": 22,
    "course": "Python",
    "marks": 85,
   
}

print("Original Dictionary:")
print(student)



# # Removes all elements from dictionary
# d1 = student.copy() #  copying the same dictonary

# # 1. clear()
# d1.clear()
# print("\n1. clear():") # it will become empty dict
# print(d1)


# # 2. copy()
# # Creates a copy of dictionary
# d2 = student.copy()
# print("\n2. copy():")
# print(d2) # i have same student dictonary in it 


# # 3. fromkeys()
# # Creates a dictionary using given keys
# keys = ["name", "age", "course"]
# d3 = dict.fromkeys(keys, "Unknown")
# print("\n3. fromkeys():")
# print(d3)


# # 4. get()
# # Returns the value of a specified key
# print("\n4. get():")
# print(student.get("name")) # rahul
# print(student.get('marks'))# 85
# print(student.get("salary", 0)) # returning non existing by assign default value



# # 5. items()
# # Returns all key-value pairs
# print("\n5. items():")
# print(student.items())

# 6. keys()
# Returns all keys
# print("\n6. keys():")
# print(student.keys())


# # 7. pop()
# # Removes the specified key
# d4 = student.copy()
# removed_value = d4.pop("age")

# print("\n7. pop():")
# print("Removed value:", removed_value)
# print(d4)


# # 8. popitem()
# # Removes the last inserted key-value pair
# d5 = student.copy()
# removed_item = d5.popitem()

# print("\n8. popitem():")
# print("Removed item:", removed_item)
# print(d5)


# # 9. setdefault()
# # Returns value if key exists
# # If key doesn't exist, creates it
# d6 = student.copy()

# d6.setdefault("city", "Bangalore")

# print("\n9. setdefault():")
# print(d6)


# # 10. update()
# # Adds new key-value pairs
# # or updates existing values
# d7 = student.copy()

# d7.update({
#     "city": "Bangalore",
#     "salary": 50000,
#     "phone":9887776777
# })

# print("\n10. update():")
# print(d7)



# # 11. values()
# # Returns all values
# print("\n11. values():")
# print(student.values())

# print("\n========== OTHER OPERATIONS ==========")

# # Access value
# print(student["name"])

# # Add new key-value pair
# student["city"] = "Bangalore"
# print(student)

# # Update value
# student["age"] = 25
# print(student)

# # Delete using del
# del student["marks"]
# print(student)

# # Check key
# print("name" in student)

# # Check key not present
# print("salary" not in student)

# # Length of dictionary
# print("Length:", len(student))


string = "aaabbccddee"

# a3b2c2d2e2


# empty = {}

# for i in string:
    
#     empty[i] = empty.get(i, 0) + 1
    
#     # {"a" } = here a is not there so defualt 0  + 1
    
#     # {"a"} = here a exists   returns 1  + 1
    
#     # {"a"} = here a exists again returns 2 + 1
    
# new_str = ""

# for key,value in empty.items():
    
#     new_str += key + str(value)
    
# print(empty)

# s = {}

# value  = s.get('key',0)

# s['key'] = value + 1

# value2 = s.get('key',0) 

# s['key'] = 2

# s['key'] = 3


'''


string = "a  a  a  b  b  c  c  d  d  e  e"
          0  1  2  3  4  5  6  7  8  9  10

prev = oth index which means a 

count = 1

loop read from 1 

prev 0 == 1 ; a ==a ; count  = 2;  prev = 1st index means a ; at i = 1

prev 1 == 2 ; a == a ; count  = 3 ; prev = 2nd index ; at i = 2

prev 2 == 3; a == b ; not equal ; prev  = 3rd index; reset the count  = 1 ; prev  = 3

adding prev and it's count to new string ==> new_str = prev + str(count)

'a3'


prev 3 == 4; b ==b ; count = 2 ; prev = 4th index; at i = 4

prev 4 == 5; b == c ; not equal ; prev  = 5thindex ; count = 1; i = 5

adding prev and it's count to new string ==> new_str = prev + str(count)

'a3b2'

prev 5 == 6; c == c; count = 2 ; prev = 6 ; at i = 7

prev 6 == 7; c == d ; not equal ; count = 1 , prev = 7 ; at i = 8

new_str = 'a3b2c2'






'''

# new = ""

# count  = 1

# prev = string[0]

# for ele in string[1:]:
    
#     if prev == ele:
        
#         count += 1
#     else:
        
#         new += prev + str(count)
        
#         count = 1
        
#         prev = ele
# new += prev + str(count)

# print(new)
        


    
    
