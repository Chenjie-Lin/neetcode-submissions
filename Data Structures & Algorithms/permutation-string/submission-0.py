class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        size = len(s1)
        count = [0] * 26
        for i in range(size):
            count[ord(s1[i]) - ord('a')] -= 1
            count[ord(s2[i]) - ord('a')] += 1

        if all(c == 0 for c in count):
                return True
        
        for i in range(size, len(s2)):
            count[ord(s2[i]) - ord('a')] += 1
            count[ord(s2[i-size]) - ord('a')] -= 1

            if all(c == 0 for c in count):
                return True

        return False