def letterCombinations(digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        res = []
        
        abc = {
            "1": "-", # to append when below 4
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        for _ in range(4 - len(digits)):
            digits += "1"

        for a in list(abc[digits[0]]):
            for b in list(abc[digits[1]]):
                for c in list(abc[digits[2]]):
                    for d in list(abc[digits[3]]):
                        add = a + b + c + d
                        res.append(add.replace("-", ""))

        
        return res if bool(res[0]) else [] # turn [''] -> []


print(letterCombinations("23"))
print(letterCombinations(""))
print(letterCombinations("9"))
print(letterCombinations("582"))
print(letterCombinations("5826"))