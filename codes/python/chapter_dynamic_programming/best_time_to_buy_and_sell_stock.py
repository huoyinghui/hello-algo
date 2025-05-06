from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        ret = 0
        # o(n)
        sort_prices = sorted(prices)

        data = {}
        for i, v in enumerate(sort_prices):
            data[v] = i

        for i in range(n):
            buy = prices[i]
            # buy_idx = data[buy]
            # if buy_idx > (i+1):
            # n^2: 是否有大于购买价格的.
            # for j in range(i, n):
            #     sell = prices[j]
            #     ret = max(sell-buy, ret)

        return ret


def main():
    # prices = [7, 6, 4, 3, 1]
    prices = [7, 1, 5, 3, 6, 4]
    ret = Solution().maxProfit(prices=prices)
    print(ret)


if __name__ == '__main__':
    main()
