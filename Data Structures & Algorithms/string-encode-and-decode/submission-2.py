class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        for s in strs:
            encodedString += (s + chr(0))
        return encodedString

    def decode(self, s: str) -> List[str]:
        strs = []
        currStr = ''
        for i in range(len(s)):
            if s[i] == chr(0):
                strs.append(currStr)
                currStr = ""
            else:
                currStr += s[i]
        return strs