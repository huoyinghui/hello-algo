

from typing import List


class Solution:
    def countNumbers(self, cnt: int) -> List[int]:
        m = 10 ** cnt
        buf = [i for i in range(1, m)]
        return buf
        

def main():
    print(Solution().countNumbers(2))

if __name__ == "__main__":
    main()
