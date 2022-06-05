class Solution:
    def maxArea(self, height: List[int]) -> int:
        # use two pointers: left and right
        # move the pointer which is smaller. Keep calculating vol. of water until left < right
        
        l, r = 0, len(height) -1
        maxVol = 0
        while l < r:
            curVol = min(height[r],height[l])*(r-l)
            if curVol > maxVol:
                maxVol = curVol
                
            if height[l] < height[r]: # move left pointer
                l+=1
            elif height[l] > height[r]: # move right pointer
                r -= 1
            else:
                l+=1
        return maxVol