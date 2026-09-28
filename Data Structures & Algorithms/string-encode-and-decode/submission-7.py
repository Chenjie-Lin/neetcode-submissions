class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += str(len(i))
            res += "#"
            res += i
        return res
    def decode(self, s: str) -> List[str]:
        print(s)
        num = ""
        res = []
        i = 0
        while i < len(s):
            if s[i] != "#":
                num += s[i]
                i += 1
            else:
                num = int(num)
                res.append(s[i+1: i + num + 1])
                i += num + 1
                num = ""
        return res
                

