def iq_test(numbers):
    n = list(map(int, numbers.split(' ')))
    odd = 0
    even = 0
    for i in range(len(n)):
        if n[i] % 2 > 0:
            even  += 1
        if n[i] % 2 == 0:
            odd  += 1
            
    for i in range(len(n)):
        if n[i] % 2 > 0 and even == 1:
            return i + 1
        if n[i] % 2 == 0 and odd == 1:
            return i + 1