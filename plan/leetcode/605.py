# 605. 种花问题
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                pass
            else:
                pass
            print(i)
        return 0


def main():
    flowerbed = [1, 0, 0, 0, 1]
    n = 1
    ret = Solution().canPlaceFlowers(flowerbed, n)
    print(ret)

if __name__ == "__main__":
    main()
