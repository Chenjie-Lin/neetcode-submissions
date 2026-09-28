class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for i in nums:
            counts[i] += 1
        res = sorted(counts, key=counts.get, reverse=True)
        return res[0:k]