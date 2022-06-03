class Solution:
        
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # iterate from 0 to n-1
        # for a[i], do binary search for (target-a[i]) in i+1 to n-1 sub array
        # if found => check if the found element is not same as a[i], if not great! else continue for  
        # next i
        n = len(numbers)
        # ret = [-1,-1]
        for i in range(n):
            to_find = target - numbers[i]
            to_find_idx = -1
            left = i+1
            right = n-1
            while right >= left:
                mid = (int)((right+left)/2)
                if numbers[mid] == to_find:
                    to_find_idx = mid
                    break
                elif numbers[mid] > to_find:
                    right = mid-1
                else:
                    left = mid+1
            if to_find_idx != -1:
                return [i+1, to_find_idx+1]
            