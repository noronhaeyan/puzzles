import pytest


class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        output = []
        temp = 0
        for num in nums:
            temp += num
            output.append(temp)

        return output


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 4], [1, 3, 6, 10]),
        ([1, 1, 1, 1, 1], [1, 2, 3, 4, 5]),
        ([3, 1, 2, 10, 1], [3, 4, 6, 16, 17]),
        ([0], [0]),
        ([5], [5]),
        ([-5], [-5]),
        ([0, 0, 0], [0, 0, 0]),
        ([-1, -2, -3], [-1, -3, -6]),
        ([1, -1, 1, -1], [1, 0, 1, 0]),
        ([10**6, 10**6, -10**6], [10**6, 2 * 10**6, 10**6]),
    ],
)
def test_running_sum(nums, expected):
    assert Solution().runningSum(nums) == expected


def test_does_not_mutate_input():
    nums = [1, 2, 3]
    Solution().runningSum(nums)
    assert nums == [1, 2, 3]


def test_matches_brute_force():
    nums = list(range(-50, 50))
    expected = [sum(nums[: i + 1]) for i in range(len(nums))]
    assert Solution().runningSum(nums) == expected


if __name__ == "__main__":
    pytest.main([__file__])
