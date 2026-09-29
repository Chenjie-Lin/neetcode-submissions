class Solution:
    def minWindow(self, s: str, t: str) -> str:

        count1 = defaultdict(int)
        count2 = defaultdict(int)
        res = ""
        best = None
        formed = 0

        if not s or not t:
            return ""

        for i in t:
            count1[i] += 1

        required = len(count1) 
        
        left = 0

        for right in range(len(s)):

            c = s[right]
            count2[c] += 1
            if c in count1 and count2[c] == count1[c]:
                formed += 1

                while formed == required:
                    if best is None or right - left + 1 < best:
                        res = s[left:right+1]
                        best = len(res)
                    c = s[left]
                    count2[c] -= 1
                    left += 1
                    if c in count1 and count2[c] < count1[c]:
                        formed -= 1


        return res
