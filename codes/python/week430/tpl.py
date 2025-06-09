from typing import List


class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        ret = 0
        for i in range(n):
            min = grid[0][i]
            last = min
            for j in range(1, m):
                cur = grid[j][i]
                target = cur
                if cur <= last:
                    target = last+1
                    ret += target - cur
                    # print(f"i {i} j {j}, cur {cur} --> {target},  min([{i}]当前列的最小值) {min}, ret {ret} ")
                last = target
        return ret


def main():
    grid = [
        [0],
        [50],
    ]
    grid = [[3, 2], [1, 3], [3, 4], [0, 1]]
    grid = [[3, 2, 1], [2, 1, 0], [1, 2, 3]]
    # grid = [
    #     [6, 3, 4],
    #     [9, 1, 3],
    #     [4, 6, 3]
    # ]
    ret = Solution().minimumOperations(grid)
    print(ret)


if __name__ == '__main__':
    main()

