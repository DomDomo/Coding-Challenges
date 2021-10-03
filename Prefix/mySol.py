def longestCommonPrefix(strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if len(strs) < 2:
            return ""

        substr = ""
        pos = 0

        for i in range(len(strs) - 1):
            for _ in range(len(min(strs[i], strs[i+1])-1)):
                if strs[i][pos] == strs[i+1][pos]:
                    substr += strs[i][pos]
                else:
                    break
                print(substr)
                pos += 1

        return substr

print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["dog","racecar","car"]))