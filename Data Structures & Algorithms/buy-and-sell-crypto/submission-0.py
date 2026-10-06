class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right, profit = 0, 1, 0
        n = len(prices) - 1

        while right <= n:

            if prices[left] > prices[right]:
                left = right
                right += 1

            else:

                temp_profit = prices[right] - prices[left]

                profit = max(profit, temp_profit)

                right += 1

        return profit


#we are going to return maximum profit
#so we have a left and right tracker
#as each day goes by we use the right, minus the left
#then we use max that day 2 day profit against the current
#if the left is bigger than right, means that the profit is negative
#then we move the left to the right pointer

#index =    0,1,2,3,4,5
#prices = [10,1,5,6,7,1]