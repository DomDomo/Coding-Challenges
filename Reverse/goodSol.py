def reverse(x: int) -> int:
        rev = int(str(abs(x))[::-1])
        return (-rev if x < 0 else rev) if rev.bit_length() < 32 else 0

print(reverse(123))
print(reverse(-123))
print(reverse(120))
print(reverse(0))
print(reverse(1534236469))