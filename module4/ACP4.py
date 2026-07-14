


n = 16


print("n       =", n, "->", bin(n))
print("n - 1   =", n - 1, "->", bin(n - 1))
print("n&(n-1) =", n & (n - 1), "->", bin(n & (n - 1)))


def is_power_of_2(num):
    return num > 0 and (num & (num - 1)) == 0



numbers = [1, 2, 4, 6, 8, 12, 16, 18, 32]

for num in numbers:
    print(num, "->", bin(num), "->", is_power_of_2(num))



def is_power_of_4(num):
    if not is_power_of_2(num):
        return False

    position = 0

    while num > 1:
        num = num >> 1
        position = position + 1

    return position % 2 == 0




for num in numbers:
    print(num, "->", is_power_of_4(num))



def is_power_of_8(num):
    if not is_power_of_2(num):
        return False

    position = 0

    while num > 1:
        num = num >> 1
        position = position + 1

    return position % 3 == 0



for num in numbers:
    print(num, "->", is_power_of_8(num))




def binary_power(base, exponent):
    answer = 1

    while exponent > 0:
        if exponent & 1:
            answer = answer * base

        base = base * base
        exponent = exponent >> 1

    return answer

print("2^5 =", binary_power(2, 5))
print("3^4 =", binary_power(3, 4))
print("5^3 =", binary_power(5, 3))


