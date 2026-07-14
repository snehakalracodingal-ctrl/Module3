
 

a = 56
b = 12
 

print("Before Swap:")
print("a =", a)
print("b =", b)
 
a = a + b
b = a - b
a = a - b
 
print("After Swap:")
print("a =", a)
print("b =", b)

x = 45
y = 18
 

print("Before XOR Swap:")
print("x =", x)
print("y =", y)
 
x = x ^ y
y = x ^ y
x = x ^ y
 
print("After XOR Swap:")
print("x =", x)
print("y =", y)
 
 
 
number = 3
 

print("Original Number:", number)
 
print(number, "<< 1 =", number << 1)
print(number, "<< 2 =", number << 2)
print(number, "<< 3 =", number << 3)
print(number, "<< 4 =", number << 4)
 
print("Each left shift multiplies the number by 2.")

num1 = -10
num2 = 5
 

print("num1 =", num1)
print("num2 =", num2)
 
if (num1 < 0) ^ (num2 < 0):
    print("The numbers have different signs.")
else:
    print("The numbers have the same sign.")
 
 

 
dividend = 25
divisor = 4
 
quotient = 0
remainder = dividend
 
while remainder >= divisor:
    remainder = remainder - divisor
    quotient = quotient + 1
 

print("Dividend:", dividend)
print("Divisor:", divisor)
print("Quotient:", quotient)
print("Remainder:", remainder)
 
