val = input("Enter a number:")
print(val)

#finding the type of the input
print(type(val))

#typecasting the input to integer
num = int(input("Enter a number:"))
print("entered number is",num)
print(type(num))
#typecasting the input to float
num1 = float(input("enter a number:"))
print("entered number is",num1)
print(type(num1))
#taking multiple inputs
x,y,z = input("enter the values of x,y,z using space:").split()
print("value of x is:",x)
print("value of y is:",y)
print("value of z is:",z)

#finding type of the object
a = "Hello World"
b = 10
c = 11.22
d = ("Geeks", "for", "Geeks")
e = ["Geeks", "for", "Geeks"]
f = {"Geeks": 1, "for":2, "Geeks":3}


print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
