

switch_value = 45   


def show_bits(number):
    return bin(number)[2:]

print("Switch Value:", switch_value)
print("Binary Form:", show_bits(switch_value))



binary_value = show_bits(switch_value)

set_bits = binary_value.count("1")
zero_bits = binary_value.count("0")

print("Set Bits / ON Switches:", set_bits)
print("Zero Bits / OFF Switches:", zero_bits)



count = 0
temp = switch_value

while temp > 0:
    if temp & 1:
        count = count + 1
    temp = temp >> 1

print("Number of ON switches:", count)




position = 1
temp = switch_value

while temp > 0:
    if temp & 1:
        break
    position = position + 1
    temp = temp >> 1

print("First ON switch is at position:", position)



for i in range(6):
    mask = 1 << i
    print("Bit", i, "Mask:", mask, "Binary:", show_bits(mask))

switch_names = [
    "Living Room Light",
    "Fan",
    "Air Conditioner",
    "Door Lock",
    "Garden Light",
    "Security Camera"]


for i in range(6):
    mask = 1 << i

    if switch_value & mask:
        print("Bit", i, "-", switch_names[i], "is ON")
    else:
        print("Bit", i, "-", switch_names[i], "is OFF")



print("Switch Value:", switch_value)
print("Binary Form:", show_bits(switch_value))
print("Total ON Switches:", count)
print("First ON Switch Position:", position)
print("================================")
