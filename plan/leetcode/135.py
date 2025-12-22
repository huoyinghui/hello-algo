from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        """
        LeetCode 135. 分发糖果 - 贪心算法（两次遍历）
        
        算法思路：
        1. 初始化每个孩子分配1颗糖果
        2. 第一次遍历（从左到右）：保证右边评分高的孩子比左边多
           - 如果 ratings[i+1] > ratings[i]，则 candy[i+1] = candy[i] + 1
        3. 第二次遍历（从右到左）：保证左边评分高的孩子比右边多
           - 如果 ratings[i-1] > ratings[i]，且 candy[i-1] <= candy[i]
           - 则 candy[i-1] = candy[i] + 1（取较大值以同时满足两个规则）
        4. 返回糖果总数
        
        时间复杂度：O(n)，空间复杂度：O(n)
        """
        # 初始化：每个孩子至少分配1颗糖果
        ret = [1] * len(ratings)
        n = len(ratings)
        
        # 第一次遍历：从左到右，处理递增序列
        # 保证评分高的孩子比左边邻居糖果多
        for i in range(0, n - 1):
            # 如果右边孩子评分更高，糖果数在左边基础上+1
            if ratings[i + 1] > ratings[i]:
                ret[i + 1] = ret[i] + 1

        # 第二次遍历：从右到左，处理递减序列
        # 保证评分高的孩子比右边邻居糖果多，同时不破坏第一次遍历的结果
        for i in range(0, n - 1):
            x = n - 1 - i  # 从右向左的索引
            # print(f"x:{x}, ret:{ret[x]}, ret-1:{ret[x-1]}")
            # 如果左边孩子评分更高
            if ratings[x - 1] > ratings[x]:
                # 只有当左边孩子糖果数不足时才更新（取max保证两个规则都满足）
                if ret[x - 1] <= ret[x]:
                    ret[x - 1] = ret[x] + 1
        
        return sum(ret)



def main():
    """
    示例 1：

输入：ratings = [1,0,2]
输出：5
解释：你可以分别给第一个、第二个、第三个孩子分发 2、1、2 颗糖果。
示例 2：

输入：ratings = [1,2,2]
输出：4
解释：你可以分别给第一个、第二个、第三个孩子分发 1、2、1 颗糖果。
     第三个孩子只得到 1 颗糖果，这满足题面中的两个条件。
    """
    ratings = [1, 0, 2]
    print(Solution().candy(ratings))

    ratings = [1, 2, 2]
    ret = Solution().candy(ratings)
    print(ret)

    ratings = [1,3,4,5,2]
    print(Solution().candy(ratings))
    pass


if __name__ == "__main__":
    main()
