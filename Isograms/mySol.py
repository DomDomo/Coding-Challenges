def is_isogram(string):
    res = True

    if(len(string) <= 1):
        return res

    # Sorted lowercase string string
    word = "".join(sorted(string.lower()))

    letter = 0
    while letter < len(word)-1:
        if word[letter] == word[letter+1]:
            res = False
            break
        letter += 1
    return res


print(is_isogram("helLo"))
print(is_isogram("hey"))
print(is_isogram("hElooOzz"))
print(is_isogram("Hh"))
print(is_isogram("hr"))
print(is_isogram("n"))
print(is_isogram(""))