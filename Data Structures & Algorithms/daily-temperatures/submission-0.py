class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        results = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev = stack.pop() #lets say it is 0
                res = i - prev # 1- 0 = 1

                results[prev] = res # results[0] = 1

            stack.append(i)
        return results

# if stack is empty append the temp

# if temp of the current day is greater than the previous day, pop the prev day indices and add the new indices into the stack. Also calculate the difference in indices and insert into results

#if temp is less than just append the temp