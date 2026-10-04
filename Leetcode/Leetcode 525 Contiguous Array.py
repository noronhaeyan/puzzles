import random

import pytest


class Solution:
    def findMaxLength(self, nums: list[int]) -> int:

        prefix = 0
        prev = {}
        prev[0] = -1
        output = 0

        for j, num in enumerate(nums):
            if num == 0:
                prefix -= 1
            else:
                prefix += 1
            if prefix in prev:
                output = max(output, j - prev[prefix])
            else:
                prev[prefix] = j

        return output


def brute_force(nums):
    best = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            sub = nums[i:j + 1]
            if sub.count(0) == sub.count(1):
                best = max(best, len(sub))
    return best


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([0, 1], 2),
        ([0, 1, 0], 2),
        ([0, 1, 1, 1, 1, 1, 0, 0, 0], 6),
        ([0], 0),
        ([1], 0),
        ([0, 0, 0], 0),
        ([1, 1, 1], 0),
        ([0, 0, 1, 1], 4),
        ([1, 0, 1, 0, 1, 0], 6),
        ([0, 0, 1, 0, 0, 0, 1, 1], 6),
        ([1, 1, 0, 0, 1], 4),
    ],
)
def test_find_max_length(nums, expected):
    assert Solution().findMaxLength(nums) == expected


def test_matches_brute_force_random():
    rng = random.Random(3)
    for _ in range(200):
        nums = [rng.randint(0, 1) for _ in range(rng.randint(1, 20))]
        assert Solution().findMaxLength(nums) == brute_force(nums)


def test_large_input():
    nums = [0, 1] * 50000
    assert Solution().findMaxLength(nums) == 100000


if __name__ == "__main__":
    pytest.main([__file__])
