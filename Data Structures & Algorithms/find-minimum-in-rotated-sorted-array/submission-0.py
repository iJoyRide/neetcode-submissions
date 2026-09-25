class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            #nums[mid] = 5

            if nums[mid] < nums[right]:
                #5!<2
                right = mid
            
            else:
                left = mid + 1

        return nums[left]


#index 0  1  2  3  4  5
#value 3  4  5  6  1  2        
        