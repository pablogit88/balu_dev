text = "hello python world  "

print(text.capitalize())
print(text.casefold())
print(text.lower())
print(text.upper())
print(text.title())
print(text.swapcase())

print(text.strip())
print(text.lstrip())
print(text.rstrip())

print(text.replace("python", "Java"))

print(text.split())
print(text.rsplit())
print("Hello\nPython".splitlines())

print("-".join(["Hello", "Python"]))

print(text.find("python"))
print(text.rfind("o"))
print(text.index("python"))
print(text.rindex("o"))

print(text.count("o"))

print(text.startswith("  Hello"))
print(text.endswith("  "))

print("Python".center(20,"*"))
print("Python".ljust(10,"*"))
print("Python".rjust(10,"*"))
print("25".zfill(5))

print("Hello {}".format("python"))
print("Hello {name}".format_map({"name": "python"}))

print("a-b-c".partition("-"))
print("a-b-c".rpartition("-"))

print("A\tB".expandtabs(4))

print("Python".encode())

print("Python".isascii())
print("Python".isalpha())
print("Python123".isalnum())
print("123".isdecimal())
print("123".isdigit())
print("123".isnumeric())
print("python".isidentifier())
print("python".islower())
print("PYTHON".isupper())
print("Python World".istitle())
print("   ".isspace())
print("Python".isprintable())


words = {'hello', 'world', 'python'} # set

# output = {'H':'ello' , 'W':'orld','P':'ython'} # dictonary

# dit = dict()

# for i in words:
    
#     dit[i[0].upper()] = i[1:]
    
# print(dit)

    
print({i[0].upper():i[1:] for i in words})


nums = [0,1,0,1,1,1,0,1,0,1,1,1,1,0] # 4 


count = 0 

maxi  = 0 


for i in nums:
    
    if i == 1: # 0 == 1 , 1 == 1, 0 == 1 ; 1 1 1 0
        
        count += 1 # 3
        
    else:
        
        if count > maxi: #0 >0  , 1 > 0 , 3 > 1 , 4 > 
            
            maxi = count # 1, 3 , 4 
        count  = 0 # 0  0 

print(maxi)
