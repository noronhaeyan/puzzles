import pytest


class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        n = len(nums)
        left = 0
        right = 0

        output = 0
        temp = 0

        for right in range(n):
            if nums[right] == 0:
                temp += 1

            while temp > k:
                if nums[left] == 0:
                    temp -= 1
                left += 1

            output = max(output, right - left + 1)

        return output


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2, 6),
        ([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3, 10),
        ([0], 0, 0),
        ([0], 1, 1),
        ([1], 0, 1),
        ([1, 1, 1, 1], 0, 4),
        ([0, 0, 0, 0], 0, 0),
        ([0, 0, 0, 0], 2, 2),
        ([0, 0, 0, 0], 4, 4),
        ([1, 0, 1, 0, 1], 0, 1),
        ([1, 0, 1, 0, 1], 1, 3),
        ([1, 0, 1, 0, 1], 2, 5),
    ],
)
def test_longest_ones(nums, k, expected):
    assert Solution().longestOnes(nums, k) == expected


def test_matches_brute_force():
    nums = [1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1]
    for k in range(len(nums) + 1):
        brute = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i:j + 1].count(0) <= k:
                    brute = max(brute, j - i + 1)
        assert Solution().longestOnes(nums, k) == brute


if __name__ == "__main__":
    pytest.main([__file__])
