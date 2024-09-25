"""
x = input("number1 :")
y = input("number2 :")

print(type(x)) # str tipte type ile kontrol edildi
print(type(y))

total = int(x)+int(y)
print(total)
"""

x = 5              
y = 2.5
name = "enes"
isOnline = True 

print(type(x))
print(type(y))
print(type(name))
print(type(isOnline))

# int to float
x = float(x)
print(x)
print(type(x))

#float to int
y = int(y)
print(y)
print(type(y))

#int and float to str
result = str(x) + str(y)
print(result)
print(type(result))

#bool to str
isOnline = str(isOnline)
print(isOnline)
print(type(isOnline))
