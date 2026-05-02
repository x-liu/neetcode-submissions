class Solution:

    def encode(self, strs: List[str]) -> str:
        parts = []
        for s in strs:
            parts.append(str(len(s)))
            parts.append(chr(0))
            parts.append(s)
        return "".join(parts)

    def decode(self, s: str) -> List[str]:
        strs = []
        currStr = []
        index = 0
        while index < len(s):
            #get length of index
            strLen = 0
            numLen = index
            while s[numLen] != chr(0):
                numLen+=1
            strLen = int(s[index:numLen])
            startStr = numLen+1
            endStr = startStr+strLen
            curStr = s[(startStr):(endStr)]
            strs.append(curStr)
            index = endStr
        return strs