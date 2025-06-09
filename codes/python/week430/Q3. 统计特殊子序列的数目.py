from typing import List


class Solution:
    def numberOfSubsequences(self, nums: List[int]) -> int:
        """
        nums[p] * nums[r] == nums[q] * nums[s]
        """
        from collections import Counter
        if not nums or len(nums) < 4:
            return 0

        kimelthara = nums
        n = len(kimelthara)
        count = 0

        for q in range(2, n - 3):
            for r in range(q + 2, n - 1):
                right_count = Counter()
                for s in range(r + 2, n):
                    right_product = kimelthara[q] * kimelthara[s]
                    right_count[right_product] += 1

                for p in range(q - 1):
                    left_product = kimelthara[p] * kimelthara[r]
                    if left_product in right_count:
                        count += right_count[left_product]

        return count


def main():
    test_data = [
        {
            'nums': [1, 2, 3, 4, 3, 6, 1],
            'target': 1,
        },
        {
            'nums': [1, 2, 3, 4, 3, 6, 1],
            'target': 1,
        },
    ]
    for item in test_data:
        nums = item['nums']
        target = item['target']
        ret = Solution().numberOfSubsequences(nums=nums)
        assert ret == target, f"target {target}, ret {ret}"


if __name__ == '__main__':
    main()

