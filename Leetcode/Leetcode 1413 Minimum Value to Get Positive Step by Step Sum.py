import pytest


class Solution:
    def minStartValue(self, nums: list[int]) -> int:
        min_temp = 101
        temp = 0
        for num in nums:
            temp += num
            min_temp = min(min_temp, temp)

        return max(1 - min_temp, 1)


def brute_force(nums):
    start = 1
    while True:
        total = start
        ok = True
        for num in nums:
            total += num
            if total < 1:
                ok = False
                break
        if ok:
            return start
        start += 1


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([-3, 2, -3, 4, 2], 5),
        ([1, 2], 1),
        ([1, -2, -3], 5),
        ([1], 1),
        ([-1], 2),
        ([0], 1),
        ([-100] * 100, 10001),
        ([100] * 100, 1),
        ([-5, 5], 6),
        ([5, -5], 1),
        ([5, -6], 2),
    ],
)
def test_min_start_value(nums, expected):
    assert Solution().minStartValue(nums) == expected


def test_matches_brute_force():
    cases = [
        [-3, 2, -3, 4, 2],
        [2, -1, -4, 3, 1, -2],
        [-10, 20, -15, 5, -1],
        [0, 0, 0],
        [-1, -1, -1, 5],
    ]
    for nums in cases:
        assert Solution().minStartValue(nums) == brute_force(nums)


if __name__ == "__main__":
    pytest.main([__file__])
