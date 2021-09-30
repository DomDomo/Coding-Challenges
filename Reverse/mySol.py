def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    
    maxN = (2**31 - 1)

    num = int(str(abs(x))[::-1])
    if num > maxN:
        return 0
    return num if x > 0 else -num
        

print(reverse(123))
print(reverse(-123))
print(reverse(120))
print(reverse(0))
print(reverse(1534236469))