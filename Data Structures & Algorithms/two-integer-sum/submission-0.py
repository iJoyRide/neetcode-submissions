class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}

        for i, num in enumerate(nums):
            answer = target - num

            if answer in hashmap:
                return [hashmap[answer], i]
            
            hashmap[num] = i