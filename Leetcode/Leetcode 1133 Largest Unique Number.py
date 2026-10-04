import random
from collections import Counter

import pytest


class Solution:
    def largestUniqueNumber(self, nums: list[int]) -> int:

        visited = set()
        visited1 = set()

        for num in nums:
            if num in visited:
                if num in visited1:
                    visited1.remove(num)
                    continue
                continue
            visited.add(num)
            visited1.add(num)

        return max(visited1) if len(visited1) > 0 else -1


def brute_force(nums):
    counts = Counter(nums)
    uniques = [n for n, c in counts.items() if c == 1]
    return max(uniques) if uniques else -1


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([5, 7, 3, 9, 4, 9, 8, 3, 1], 8),
        ([9, 9, 8, 8], -1),
        ([0], 0),
        ([1000], 1000),
        ([5, 5], -1),
        ([5, 5, 5], -1),
        ([5, 5, 5, 3], 3),
        ([1, 2, 3], 3),
        ([0, 0, 1], 1),
        ([0, 0, 1, 1], -1),
        ([2, 2, 2, 2, 1], 1),
    ],
)
def test_largest_unique_number(nums, expected):
    assert Solution().largestUniqueNumber(nums) == expected


def test_matches_brute_force_random():
    rng = random.Random(2)
    for _ in range(200):
        nums = [rng.randint(0, 10) for _ in range(rng.randint(1, 30))]
        assert Solution().largestUniqueNumber(nums) == brute_force(nums)


if __name__ == "__main__":
    pytest.main([__file__])
