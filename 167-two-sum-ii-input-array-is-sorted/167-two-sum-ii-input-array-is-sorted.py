class Solution:
        
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # use 2 pointers: low=0, high=n-1. 
        # if low+high > target => high_idx--
        # if low+high < target => low_idx++
        # else return [low_idx +1, high_idx+1]
        n = len(numbers)
        low = 0
        high = n-1
        while(low < high):
            if numbers[low] + numbers[high] > target:
                high -= 1
            elif numbers[low] + numbers[high] < target:
                low += 1
            else:
                return [low+1, high+1]
        
        
            