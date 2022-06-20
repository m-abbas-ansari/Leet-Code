class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Do 2 passes through nums array: 
        # left -> right for prefix product 
        # right -> left for postfix product
        # You can just use the output array to store the resultant pre*post
        # O(n) time, O(1) space complexity
        
        res = []
        prefix = 1
        for n in nums: # traversing left -> right
            res.append(prefix)
            prefix *= n
        postfix = 1
        for i in range(len(nums)-1, -1, -1): # traversing right -> left
            res[i] *= postfix
            postfix *= nums[i]
        
        return res
            
        
        