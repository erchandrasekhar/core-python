# Arithmetic operators
print("######################### Arithmetic operators ###########################")
x = 16
y = 5
print("addition of two number      :",x+y)
print("substation of two number    :",x-y)
print("division of two number      :",x/y)
print("multiplication of two number:",x*y)
print("modulus of two number       :",x%y)

#Python Assignment Operators
print("###################### Python Assignment Operators ####################")

x = 3
y = x+3
z = x-3
p = x -3
q = x/2

print(x,y,z,p,q)

#Python Comparison Operators
print("#############################Python Comparison Operators####################")
x = 25
y = 12
if x > y:
     print("x > y")
elif x < y:
     print("x< y")
elif x >= y:
     print("X>= y")
elif x <= y:
     print("X <= y")

else:
     print("hello")

#Python Logical Operators
print("######################Python Logical Operators#######################")

x,y = 20,25
if x <30 and y <30:
     print("true")
elif x < 10 and y <10:
     print("false")
# Python Identity Operators

x = 20
y = 22
if x is y:
     print("x and y are equal")
elif x is not y:
     print("x and y are not equal")

#Python Membership Operators
print("########################    #Python Membership Operators     ################################")
str = ["chandrasekhar","kalpana","anand","ashok"]

x = "555"

if x in str:
     print(" yes  x  anand is present in list at")
else:
     print(" x not present in list")






