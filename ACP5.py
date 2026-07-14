#lcm of 2 numbers enter 2 numbers
from matplotlib.pylab import gcd


num1 = int(input("Enter first number: "))   
num2 = int(input("Enter second number: "))
lcm = (num1 * num2) // gcd(num1, num2)
print("The LCM of", num1, "and", num2, "is", lcm)