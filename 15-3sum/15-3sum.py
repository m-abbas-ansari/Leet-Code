class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Iterate through nums to choose a number -> a[i]
        # then do 2-sum for remaining nums array where target = 0 - a[i]
        # 2 - sum: Make a dictionary where keys are the elements of nums array
        
        result = []
        
        while len(nums) != 0:
            n = nums[0]
            target = 0 - n
            nums.remove(n)
            d = {}
            for j, p in enumerate(nums): # perform 2-sum for target
                b = target - p
                if b in d:
                    res = [n,p,b]
                    res.sort()
                    if res not in result:
                        result.append(res)
                d[p] = j
         
        return result