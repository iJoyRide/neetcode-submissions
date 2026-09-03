class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for n in num_set:
            count = 0
            if (n-1) in num_set:
                continue

            length = 1
            current = n

            while (current +1) in num_set:
                current += 1     
                length += 1

            longest = max(longest,length)
        
        return longest

        