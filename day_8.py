'''
set is a data structure is used to store large amount by not allowing 

duplicates in it

it defines with curly brace 

it does not contain indexing


it is not mutable


add

remove

discard

update

clear

copy


'''
# new = {1,2,3,4,5,5}

# new.add(6)

# new.remove(2)

# new.discard(8)

# print(new)

# new.update([5,7])

# print(new)


# news  = new.copy()

# print(news)

# news.clear()

# print(news)

# # ==================================================
# #        SET OPERATIONS - ALL IN ONE SHOT
# # ==================================================

# A = {10, 20, 30, 40}
# B = {30, 40, 50, 60}

# print("A =", A)
# print("B =", B)

# --------------------------------------------------
# 1. union()  -> Combines both sets (No duplicates)
# # --------------------------------------------------
# print("\n1. union()")
# print("A.union(B) =", A.union(B))
# print("A | B      =", A | B)

# # --------------------------------------------------
# # 2. intersection() -> Common elements
# # --------------------------------------------------
# print("\n2. intersection()")
# print("A.intersection(B) =", A.intersection(B))
# print("A & B             =", A & B)

# # --------------------------------------------------
# # 3. difference() -> Elements in A but not in B
# # --------------------------------------------------
# print("\n3. difference()")
# print("A.difference(B) =", A.difference(B))
# print("A - B           =", A - B)

# print("B.difference(A) =", B.difference(A))
# print("B - A           =", B - A)

# # --------------------------------------------------
# # 4. symmetric_difference()
# # Elements present in either set but NOT both
# # --------------------------------------------------
# print("\n4. symmetric_difference()")
# print("A.symmetric_difference(B) =", A.symmetric_difference(B))
# print("A ^ B                     =", A ^ B)

# # --------------------------------------------------
# # 5. intersection_update()
# # Keeps only common elements (Modifies original set)
# # --------------------------------------------------
# print("\n5. intersection_update()")

# X = {10, 20, 30, 40}
# Y = {30, 40, 50, 60}

# print("Before:", X)
# X.intersection_update(Y)
# print("After :", X)

# # --------------------------------------------------
# # 6. difference_update()
# # Removes elements that are common (Modifies original)
# # --------------------------------------------------
# print("\n6. difference_update()")

# X = {10, 20, 30, 40}
# Y = {30, 40, 50, 60}

# print("Before:", X)
# X.difference_update(Y)
# print("After :", X)

# # --------------------------------------------------
# # 7. symmetric_difference_update()
# # Keeps only non-common elements (Modifies original)
# # --------------------------------------------------
# print("\n7. symmetric_difference_update()")

# X = {10, 20, 30, 40}
# Y = {30, 40, 50, 60}

# print("Before:", X)
# X.symmetric_difference_update(Y)
# print("After :", X)


# numbers = {5, 10, 15, 20}

# print("\n===== Built-in Functions =====")

# print("len()      :", len(numbers))
# print("max()      :", max(numbers))
# print("min()      :", min(numbers))
# print("sum()      :", sum(numbers))
# print("sorted()   :", sorted(numbers))   # Returns list
# print("any()      :", any(numbers))
# print("all()      :", all(numbers))


# numbers = {5, 10, 0, 20}

'''

sets stores the values based on hash function



'''

# print("\n===== Built-in Functions =====")

# print("len()      :", len(numbers))
# print("max()      :", max(numbers))
# print("min()      :", min(numbers))
# print("sum()      :", sum(numbers))
# print("sorted()   :", sorted(numbers))   # Returns list
# print("any()      :", any(numbers))
# print("all()      :", all(numbers))

# '''

# data structure conversions

# list - > set

# tuple -> set

# '''

# lists = (1,2,3,4,5,6,7,7,7,7,8)

# # for duplicate removal we can simply convert into set

# news = set(lists)

# print(news)

# new_Set  = set()

# for i in lists:
    
#     if i not in new_Set:
        
#         new_Set.add(i)
# print(new_Set)



# unique = [1,2,3,4,5,6,7,8,9,9,9,9,9,9,9]

# # print(len(set(unique)))



# print(hash('a'))

# print(hash('b'))


# | Method                          | Meaning                       | Modifies Original? |
# | ------------------------------- | ----------------------------- | ------------------ |
# | `union()`                       | Combine all unique elements   | ❌ No               |
# | `intersection()`                | Common elements               | ❌ No               |
# | `difference()`                  | Elements only in first set    | ❌ No               |
# | `symmetric_difference()`        | Elements not common to both   | ❌ No               |
# | `intersection_update()`         | Keep only common elements     | ✅ Yes              |
# | `difference_update()`           | Remove common elements        | ✅ Yes              |
# | `symmetric_difference_update()` | Keep only non-common elements | ✅ Yes              |




