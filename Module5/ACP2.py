

def linear_recursion(n):
    if n == 0:
        return

    print("Linear call at level:", n)
    linear_recursion(n - 1)


print("\nPART 1: Linear Recursion")
linear_recursion(5)

def tail_recursion(n):
    if n == 0:
        return

    print("Tail work before call:", n)
    tail_recursion(n - 1)


print("\nPART 2: Tail Recursion")
tail_recursion(5)




def head_recursion(n):
    if n == 0:
        return

    head_recursion(n - 1)
    print("Head work after call:", n)


print("\nPART 3: Head Recursion")
head_recursion(5)




def increasing_decreasing(n):
    if n == 0:
        return

    print("Going down:", n)
    increasing_decreasing(n - 1)
    print("Coming back:", n)


print("\nPART 4: Increasing-Decreasing Recursion")
increasing_decreasing(5)



def tree_recursion(n):
    if n == 0:
        return

    print("Tree node:", n)
    tree_recursion(n - 1)
    tree_recursion(n - 1)


print("\nPART 5: Tree Recursion")
tree_recursion(3)
