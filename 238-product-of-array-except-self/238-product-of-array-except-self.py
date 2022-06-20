class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        pre, suf = 1, 1
        prefix.append(pre)
        suffix.insert(0, suf)
        for i in range(0, len(nums)-1):
            pre *= nums[i]
            suf *= nums[-(i+1)]
            prefix.append(pre)
            suffix.insert(0, suf)

        res = []
        for i, n in enumerate(nums):
            res.append(int((prefix[i] * suffix[i])))
        
        return res
        