class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        newdict = defaultdict(int)

        for num in nums:
            newdict[num] += 1

        sortedlist = sorted(newdict.items(), key = lambda t: t[1])

        result = []

        for pair in sortedlist[-k:]:
            result.append(pair[0])

        return result
