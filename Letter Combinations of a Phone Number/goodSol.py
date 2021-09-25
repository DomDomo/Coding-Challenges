def letterCombinations(digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if digits == '': return []
        abc = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        res=['']
        for num in digits:
            print(res)
            tmp=[]
            for inRes in res:
                for letter in abc[num]:
                    tmp.append(inRes+letter)
            res=tmp
        
        return res


print(letterCombinations("23"))
print(letterCombinations(""))
print(letterCombinations("9"))
print(letterCombinations("582"))
print(letterCombinations("5826"))