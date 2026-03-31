#Operators in python    
a=69
b=33
#Arithmetic operators
print("Addition:", a + b)  
print("Subtraction:", a - b) 
print("Multiplication:", a * b)  
print("Division:", a / b) 
print("Floor Division:", a // b)  
print("Modulus:", a % b) 
print("Exponentiation:", a ** b)
#Comparison operators
print("Equal to:", a == b)
print("Not equal to:", a != b)
print("Greater than:", a > b)
print("Less than:", a < b)
print("Greater than or equal to:", a >= b)
print("Less than or equal to:", a <= b)
#Logical operators
a = True
b = False
#precedence of logical operators: not > and > or
print("logical NOT:", not a)
print("logical AND:", a and b)
print("logical OR:", a or b)
#Bitwise operators
a = 5  
b = 3  
print("Bitwise AND:", a & b)
print("Bitwise OR:", a | b)
print("Bitwise XOR:", a ^ b)
print("Bitwise NOT:", ~a)
print("Left Shift:", a << 1)
print("Right Shift:", a >> 1)
#Assignment operators
x = 10
x += 5  # Equivalent to x = x + 5
print("After += operator:", x)
x -= 3  # Equivalent to x = x - 3
print("After -= operator:", x)
x *= 2  # Equivalent to x = x * 2
print("After *= operator:", x)
x /= 4  # Equivalent to x = x / 4
print("After /= operator:", x)
x //= 2  # Equivalent to x = x // 2
print("After //= operator:", x)
x %= 3  # Equivalent to x = x % 3
print("After %= operator:", x)
x **= 2  # Equivalent to x = x ** 2
print("After **= operator:", x)
#Membership operators
my_list = [1, 2, 3, 4, 5]
print("Is 3 in the list?", 3 in my_list)
print("Is 6 not in the list?", 6 not in my_list)
#Identity operators
a = [1, 2, 3]
b = a
print("a is b:", a is b)  # True, because a and b refer to the same object
c = [1, 2, 3]
print("a is c:", a is c)  # False, because a and c refer to different objects
print("a == c:", a == c)  # True, because a and c have the same content


