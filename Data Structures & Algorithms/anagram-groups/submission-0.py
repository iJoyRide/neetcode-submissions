class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            sortedS = sorted(s)
            newS = ",".join(sortedS)
            res[newS].append(s)

        return list(res.values())