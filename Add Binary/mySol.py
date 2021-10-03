def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """

    rmnd = 0
    a = max(a, b)
    b = (len(max(a, b)) - len(min(a, b)))*"0" + min(a, b)

    res = ""
    for pos in range(len(a)):
        num = int(a[::-1][pos]) + int(b[::-1][pos]) + rmnd
        if num > 0:
            res += "1"
        else:
            res += "0"

        rmnd = 1 if num == 2 else 0

    return res[::-1]

print(addBinary("11", "1"))
print(addBinary("1010", "1011"))
print(addBinary("0", "0"))