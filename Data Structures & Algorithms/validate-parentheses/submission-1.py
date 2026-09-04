class Solution:
    def isValid(self, s: str) -> bool:
        stackS = []
        dictS = {')':'(','}':'{',']':'[',} 

        for bracket in s:
            if bracket in dictS:
                if len(stackS) == 0:
                    return False
                if stackS.pop(-1) != dictS[bracket]:
                    return False

            else:
                stackS.append(bracket)
        
        return len(stackS) == 0

