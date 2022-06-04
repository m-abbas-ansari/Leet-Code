class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the nums array
        # select 1st element in nums array, delete that element from nums
        # using 2-pointers approach, perform 2-sum to find 2 elements which sum up to 0 - a.
        
        result = []
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and nums[i-1] == a:
                continue
            target = 0 - a

            low, high = i+1, len(nums)-1
            while low < high:
                r = nums[high] + nums[low]
                if r > target:
                    high -= 1
                elif r < target:
                    low += 1
                else:
                    result.append([a, nums[low], nums[high]])
                    l = nums[low]
                    low+=1
                    while low < high and nums[low] == l:
                        low+=1
  
        return result