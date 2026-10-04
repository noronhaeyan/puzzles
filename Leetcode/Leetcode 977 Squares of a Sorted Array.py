import pytest


class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)

        i = 0
        j = n - 1
        idx = n - 1
        output = [None] * n

        while i <= j:
            if nums[i] * nums[i] >= nums[j] * nums[j]:
                output[idx] = nums[i] * nums[i]
                idx -= 1
                i += 1
            else:
                output[idx] = nums[j] * nums[j]
                idx -= 1
                j -= 1

        return output


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100]),
        ([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121]),
        ([5], [25]),
        ([-5], [25]),
        ([0], [0]),
        ([1, 2, 3, 4], [1, 4, 9, 16]),
        ([-4, -3, -2, -1], [1, 4, 9, 16]),
        ([-3, -3, 3, 3], [9, 9, 9, 9]),
        ([-10000, 10000], [100000000, 100000000]),
        ([-2, 0, 2], [0, 4, 4]),
    ],
)
def test_sorted_squares(nums, expected):
    assert Solution().sortedSquares(nums) == expected


def test_matches_brute_force():
    nums = sorted([-9, -6, -1, 0, 2, 4, 4, 8])
    assert Solution().sortedSquares(nums) == sorted(x * x for x in nums)


if __name__ == "__main__":
    pytest.main([__file__])
