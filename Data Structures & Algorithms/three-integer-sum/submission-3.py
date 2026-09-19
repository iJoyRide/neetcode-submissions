class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        newnum = sorted(nums)
        lists = []

        for i in range(len(newnum)):
            if i !=0 and newnum[i] == newnum[i-1] :
                continue

            target = 0 - newnum[i]

            left = i + 1

            right = len(newnum) -1

            while left < right:

                if newnum[left] + newnum[right] == target:
                    lists.append([newnum[i], newnum[left], newnum[right]])
                    left += 1
                    right -= 1

                    while left < right and newnum[left] == newnum[left-1]:
                        left += 1

                elif newnum[left] + newnum[right] < target:
                    left += 1
                else:
                    right -= 1
                
        return lists
                                


#index:  0   1   2  3  4  5
#value: -4  -1  -1  0  1  2