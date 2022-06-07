class Solution:
    def trap(self, height: List[int]) -> int:
        tot_water = 0 
        l, r = 0, len(height) - 1
        h_water = 0
        while r-l > 1:
            #print("\n")
            cur_h =  min(height[l], height[r])
            #print(f"h_l = {height[l]}, h_r = {height[r]}, cur_h = {cur_h} and h_water = {h_water}")
            if cur_h > h_water:
                height_diff = cur_h - h_water
                h_water = cur_h
                tot_water += height_diff * (r - l - 1)
                #print(f"height_diff = {height_diff} tot_water = {tot_water}")
         
            if height[l] <= height[r]:
                l += 1
                if height[l] > h_water:
                    tot_water -= h_water
                else:
                    tot_water -= height[l]
                #print(f"incrementing left => tot_water = {tot_water}")
               
            
            elif height[r] < height[l]:
                r -= 1
                if height[r] > h_water:
                    tot_water -= h_water
                else:
                    tot_water -= height[r]
                #print(f"decrementing right => tot_water = {tot_water}")
                
        return tot_water