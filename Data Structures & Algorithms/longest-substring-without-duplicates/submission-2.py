class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        
        left = 0
        right = 0

        hashmap = {}

        while right < len(s):
            
            if s[right] in hashmap:
                left = max(left, hashmap[s[right]] + 1)
            
            hashmap[s[right]] = right
            longest = max(longest, (right - left + 1))
            right += 1
        
        return longest
            


# declare left and right pointers, both starting at index 0
# hashset holds the characters currently inside the window [left, right]
# outer loop: walk right across s until right reaches len(s)
#   inner loop: while s[right] is already in the hashset (duplicate),
#     remove s[left] from the hashset and move left up by 1
#     -> stops once the old copy of s[right] has been removed
#   add s[right] to the hashset (window is now duplicate-free)
#   compare longest with the current window length (right - left + 1)
#     -> do this every step, not only after a duplicate
#   move right up by 1

# ptr  L      R 
# s = "abcdzxyzxyz"
# window grows to "abcdzxy" (length 7)
# at the 2nd "z": remove a, b, c, d, z -> left = 5, window "xyz"
# at the 2nd "x": remove x -> window "yzx", and so on
# answer = 7







