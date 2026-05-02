class Solution:

    def encode(self, strs: List[str]) -> str:
        parts = []
        for s in strs:
            parts.append(s)
            parts.append(chr(0))
        return "".join(parts)

    def decode(self, s: str) -> List[str]:
        strs = []
        currStr = []
        for i in range(len(s)):
            if s[i] == chr(0):
                strs.append("".join(currStr))
                currStr = []
            else:
                currStr.append(s[i])
        return strs