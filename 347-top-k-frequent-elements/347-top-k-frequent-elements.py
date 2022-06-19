class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
        top_freq = sorted(freq.items(), key=lambda item: item[1], reverse=True)
        return [a[0] for a in top_freq[:k]]