def to_binary(value: int, bits: int) -> str:
    mask = (1 << bits) - 1
    return format(value & mask, f"0{bits}b")

number = int(input("Enter a number: "))
bits = int(input("Enter bit length: "))

mask = (1 << bits) - 1

value = number & mask
twos_complement = (~number + 1) & mask

print(f"Number: {number}")
print(f"Binary: {to_binary(value, bits)}")
print(f"2's complement: {to_binary(twos_complement, bits)}")
print(f"Negative Number: {int(~number +1)}")