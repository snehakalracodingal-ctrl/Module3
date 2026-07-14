

print("=== Dream Recursion Lab ===")
print("Two rules of recursion:")
print("  1. Call yourself with a SMALLER problem each time")
print("  2. Have a BASE CASE that stops the calls")
print()




def count_up(n):
    if n > 10:          # base case: stop here
        return
    print(n, end=" ")
    count_up(n + 1)     # recursive call: n grows toward the base case

print("Counting 1 to 10 using recursion:")
count_up(1)
print()
print()



def countdown(n):
    if n == 0:         
        print("Liftoff!")
        return
    print(n, end=" ")
    countdown(n - 1)   

print("Countdown (builds down, unwinds up):")
countdown(5)


def factorial(n):
    if n == 0 or n == 1:            # base case
        return 1
    return n * factorial(n - 1)     # recursive call: n shrinks

print("Factorial using recursion:")
print("factorial(5) =", factorial(5))
print("factorial(4) =", factorial(4))
print("factorial(1) =", factorial(1))
print("factorial(0) =", factorial(0))
print()




import sys
print("Python recursion limit:", sys.getrecursionlimit(), "calls")

def no_base_case(n):
    print("Call", n, end=" ")
    no_base_case(n + 1)   # no base case -- this never stops!

sys.setrecursionlimit(30)   # tiny limit for safe demonstration
try:
    no_base_case(1)
except RecursionError:
    print()
    print("RecursionError! Stack overflow -- no base case!")

sys.setrecursionlimit(1000)
print("Rule: ALWAYS include a base case in every recursive function!")
