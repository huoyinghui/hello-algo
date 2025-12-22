from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        """
        g: 孩子胃口值
        s: 饼干尺寸

        return 满足的孩子数量
        """
        g.sort()
        s.sort()
        i = 0 # 孩子索引
        j = 0 # 饼干索引
        while i < len(g) and j < len(s):
            # 如果孩子胃口值小于饼干尺寸，则孩子满足
            if g[i] <= s[j]:
                i += 1
            j += 1
        return i

"""
示例 1:

输入: g = [1,2,3], s = [1,1]
输出: 1
解释: 
你有三个孩子和两块小饼干，3 个孩子的胃口值分别是：1,2,3。
虽然你有两块小饼干，由于他们的尺寸都是 1，你只能让胃口值是 1 的孩子满足。
所以你应该输出 1。
示例 2:

输入: g = [1,2], s = [1,2,3]
输出: 2
解释: 
你有两个孩子和三块小饼干，2 个孩子的胃口值分别是 1,2。
你拥有的饼干数量和尺寸都足以让所有孩子满足。
所以你应该输出 2。

"""

if __name__ == "__main__":
    solution = Solution()
    g = [1, 2, 3]
    s = [1, 1]
    print(solution.findContentChildren(g, s))

    g = [1, 2]
    s = [1, 2, 3]
    print(solution.findContentChildren(g, s))

    g = [1, 2, 3]
    s = [3]
    print(solution.findContentChildren(g, s))