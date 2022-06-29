class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_hash = set(nums)
        maxlen = 0
        for n in nums:
            if n-1 not in num_hash:
                # found a start
                s = n
                l = 1
                while s+1 in num_hash:
                    s+=1
                    l+=1
                maxlen = max(l, maxlen)
        
        return maxlen