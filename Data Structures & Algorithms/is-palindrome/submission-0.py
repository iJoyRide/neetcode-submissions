class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = ''.join(c.lower() for c in s if c.isalnum())
        left = 0
        right = len(x) - 1

        while left < right:
            if x[left] != x[right]:
                return False

            left += 1
            right -= 1


        return True