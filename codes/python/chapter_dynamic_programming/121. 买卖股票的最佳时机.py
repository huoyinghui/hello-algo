from itertools import count
from math import inf
from typing import List
from functools import lru_cache


class Solution:
    """
    定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。



示例 1：

输入：[7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
示例 2：

输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 没有交易完成, 所以最大利润为 0。

    """

    def maxProfit(self, prices: List[int]) -> int:
        """
         经典 DP 模板是：
            1.	状态定义：dp[i] / dp[i][j] 是什么含义？代表什么子问题？
            2.	转移方程：从哪些状态转移到当前状态？
            3.	初始化：边界情况如何设置？
            4.	遍历顺序：从前往后 or 递归记忆化？
            5.	返回值：最终要求解的状态是哪个？
        """
        if not prices:
            return 0
        n = len(prices)
        # 1.dp[i]: 表示最大利润
        dp = [0] * (n+1)
        dp[1] = 0
        dp[2] = prices[1] - prices[0]
        # 递推公式. 最大利润: = 当天卖出价格 - 历史最低价格
        ret = 0
        for i in range(3, n+1):
            sell = prices[i-1]
            buy_min = min(prices[0:i-1])
            dp[i] = sell - buy_min
            ret = max(dp[i], ret)
        # 5.返回最大利润
        return ret

    def maxProfitV2(self, prices: List[int]) -> int:
        """
         经典 DP 模板是：
            1.	状态定义：dp[i] / dp[i][j] 是什么含义？代表什么子问题？
            2.	转移方程：从哪些状态转移到当前状态？
            3.	初始化：边界情况如何设置？
            4.	遍历顺序：从前往后 or 递归记忆化？
            5.	返回值：最终要求解的状态是哪个？

        状态定义：只需要两个变量：
            •	min_price: 记录到当前位置为止的最低价格。
            •	max_profit: 记录当前能获得的最大利润
        """
        if not prices:
            return 0
        n = len(prices)
        if n < 2:
            return 0
        if n == 2:
            return max(0, prices[1]-prices[0])
        # 1.dp[i]: 表示最大利润
        # 递推公式. 最大利润: = 当天卖出价格 - 历史最低价格
        min_price = min(prices[0], inf)
        ret = max(0, prices[1]-prices[0])
        for i in range(3, n+1):
            min_price = min(prices[i-2], min_price)
            # 递推公式. 最大利润: = 当天卖出价格 - 历史最低价格
            sell = prices[i-1]
            # O(n) -> O(1): 历史价格是固定的，可以在迭代中计算出
            ret = max(sell - min_price, ret)
        # 5.返回最大利润
        return ret

    def maxProfitV3(self, prices: List[int]) -> int:
        """
        状态定义：只需要两个变量：
            •	min_price: 记录到当前位置为止的最低价格。
            •	max_profit: 记录当前能获得的最大利润
        """
        if not prices:
            return 0
        # 历史最低价格
        min_price = min(prices[0], inf)
        # 最大利润
        max_profit = 0
        for price in prices[1:]:
            # 迭代最小价格
            min_price = min(min_price, price)
            # 迭代最大利润
            max_profit = max(max_profit, price-min_price)
        # 5.返回最大利润
        return max_profit

    def maxProfitV4(self, prices: List[int]) -> int:
        """
        状态定义：只需要两个变量：
            •	min_price: 记录到当前位置为止的最低价格。
            •	max_profit: 记录当前能获得的最大利润

        经典 DP 模板是：
            1.	状态定义：dp[i] / dp[i][j] 是什么含义？代表什么子问题？
            2.	转移方程：从哪些状态转移到当前状态？
            3.	初始化：边界情况如何设置？
            4.	遍历顺序：从前往后 or 递归记忆化？
            5.	返回值：最终要求解的状态是哪个？

        """
        # dp[i]: 表示第i天卖出获取的利润. 最优策略是：在 [0, i-1] 区间中以最低价买入
        # 所以 dp[i] = prices[i] - min(prices[0...i-1])
        # 但为了避免重复计算 min()，我们维护一个变量 min_price 即可。 O(n) -> O(1)
        return


def main():
    # prices = [7, 6, 4, 3, 1]
    # prices = [7, 1, 5, 3, 6, 4]
    # prices = [0]
    # prices = [1]
    # prices = [1, 2]
    prices = [1, 4, 2]
    ret = Solution().maxProfitV3(prices=prices)
    print(ret)


if __name__ == '__main__':
    main()



"""
“买卖股票的最佳时机” 是 LeetCode 中最经典的一类动态规划问题。它有多个变种，下面我以最基础版本：只能交易一次为例（LeetCode 121），逐步分析它的解法与动态规划思想。

⸻

🧾 题目描述：LeetCode 121 — 买卖股票的最佳时机

给定一个数组 prices，prices[i] 表示第 i 天的股票价格。你只能选择一天买入，并选择之后的一天卖出，求最大利润。

⸻

🧠 朴素思路（暴力）

对每一对 (i,j)（j > i），计算 prices[j] - prices[i]，取最大值。

时间复杂度 O(n²)，会超时。

⸻

✅ 优化思路（一次遍历）

我们记录历史最低价 min_price，并随时计算：

当前价格 - 历史最低价 = 当前最大利润

🌟 状态变量分析：
	•	min_price：目前为止看到的最低价格
	•	max_profit：目前为止可以获得的最大利润

伪代码：

min_price = prices[0]
max_profit = 0
for price in prices:
    min_price = min(min_price, price)
    max_profit = max(max_profit, price - min_price)
return max_profit


⸻

💡 动态规划角度分析（进阶理解）

这题可以不需要显式 dp 数组，但也可以套用 DP 模板分析：

1. 状态定义：
	•	设 dp[i] 为第 i 天卖出时的最大利润

2. 状态转移方程：
	•	如果我们在第 i 天卖出股票，最优策略是：在 [0, i-1] 区间中以最低价买入
	•	所以 dp[i] = prices[i] - min(prices[0...i-1])

但为了避免重复计算 min()，我们维护一个变量 min_price 即可。

⸻

🧮 举例演示：

prices = [7, 1, 5, 3, 6, 4]

i	prices[i]	min_price	profit = prices[i] - min_price	max_profit
0	7	7	0	0
1	1	1	0	0
2	5	1	4	4
3	3	1	2	4
4	6	1	5	5 ✅
5	4	1	3	5

答案就是 5

⸻

🎯 总结

点	内容
思维	不需要真 dp 数组，贪心+记忆历史最优
实质	当前利润 = 当前价格 - 之前最小价格
状态压缩	min_price 与 max_profit 足以


⸻

是否需要我讲讲这个问题的进阶版本？例如：
	•	LeetCode 122：不限交易次数
	•	LeetCode 123：最多交易两次
	•	LeetCode 309：含冷冻期
	•	LeetCode 714：含交易手续费

这些都用“状态机动态规划”可以解。要讲哪一版？
"""