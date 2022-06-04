class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the nums array
        # select 1st element in nums array, delete that element from nums
        # using 2-pointers approach, perform 2-sum to find 2 elements which sum up to 0 - a.
        
        result = []
        nums.sort()
        i = 0
        while i < len(nums):
            a = nums[i]
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
                    while low < len(nums) and nums[low] == l:
                        low+=1
            i+= 1
            while i < len(nums) and nums[i] == a:
                i+= 1
                
        return result