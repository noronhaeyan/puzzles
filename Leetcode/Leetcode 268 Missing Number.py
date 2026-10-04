import random

import pytest


class Solution:
    def missingNumber(self, nums: list[int]) -> int:

        output = set(range(len(nums) + 1))

        for num in nums:
            output.remove(num)

        return output.pop()


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([3, 0, 1], 2),
        ([0, 1], 2),
        ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
        ([0], 1),
        ([1], 0),
        ([1, 2], 0),
        ([0, 2], 1),
        ([1, 2, 3, 4], 0),
        ([0, 1, 2, 3], 4),
        (list(range(1, 10001)), 0),
        (list(range(10000)), 10000),
    ],
)
def test_missing_number(nums, expected):
    assert Solution().missingNumber(nums) == expected


def test_does_not_mutate_input():
    nums = [3, 0, 1]
    Solution().missingNumber(nums)
    assert nums == [3, 0, 1]


def test_matches_sum_formula_random():
    rng = random.Random(0)
    for n in range(1, 60):
        full = list(range(n + 1))
        missing = rng.choice(full)
        nums = [x for x in full if x != missing]
        rng.shuffle(nums)
        assert Solution().missingNumber(nums) == n * (n + 1) // 2 - sum(nums) == missing


if __name__ == "__main__":
    pytest.main([__file__])
