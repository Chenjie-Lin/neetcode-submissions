class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashset = defaultdict(int)
        left = 0
        max_freq = 0
        res = 0
        for right in range(len(s)):
            hashset[s[right]] += 1
            max_freq = max(hashset[s[right]], max_freq)

            while (right - left + 1) - max_freq > k:
                hashset[s[left]] -=1
                left += 1

            res = max(res, right - left + 1)
        return res
