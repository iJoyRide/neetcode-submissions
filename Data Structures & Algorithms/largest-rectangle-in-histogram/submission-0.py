class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        n = len(heights)

        for i in range(n):

            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                r = i
                if stack:
                    l = stack[-1]
                else:
                    l = -1
                w = r - l - 1
                area = h * w

                max_area = max(max_area, area)

            stack.append(i)

        while stack:
            h = heights[stack.pop()]
            r = n
            if stack:
                l = stack[-1]
            else:
                l = -1
            w = r - l - 1
            area = h * w

            max_area = max(max_area, area)
    
        return max_area
    

#first condition, if the stack is empty, if it is append it, for this append index 0 for h 7

#second condition, if height of the next index is shorter, pop the stack.
        
#once in the while loop, we pop the previous index, get its height and 
#measure its area and add it to the max_area


#[1,5,6,2]


        #
    #   #
    #   #
    #   #
    #   #   #
#   #   #   #