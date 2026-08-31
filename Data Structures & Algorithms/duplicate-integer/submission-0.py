class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set2 = set(nums)

        if len(set2) != len(nums):
            return True
        
        return False