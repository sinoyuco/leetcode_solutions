class Solution:
    def maxArea(self, height: List[int]) -> int:
        #         if(len(height))==2:
        #             return min(height[0],height[1])
        #         maxv = 0
        #         left,right = len(height)//2, len(height)//2+1

        #         for i in range(left,-1,-1):
        #             curr_area = min(height[i],height[right]) * (right-i)
        #             if curr_area > maxv:
        #                 maxv = curr_area
        #                 left = i

        #         for j in range(right, len(height)):
        #             curr_area = min(height[j], height[left]) * (j-left)
        #             if curr_area > maxv:
        #                 maxv = curr_area
        #                 right = j
        #         return maxv

        maxv = l = 0
        r = len(height)-1
        while l < r:
            maxv = max(maxv, min(height[l], height[r])*(r-l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxv
