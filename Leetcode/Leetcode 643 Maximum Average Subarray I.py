import pytest


class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        n = len(nums)
        left = 0
        right = k - 1
        curr = 0
        output = 0
        for i in range(k):
            curr += nums[i]
        output = curr

        for i in range(k, n):
            curr = curr + nums[i] - nums[i - k]
            output = max(output, curr)

        return output / k


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([1, 12, -5, -6, 50, 3], 4, 12.75),
        ([5], 1, 5.0),
        ([-1], 1, -1.0),
        ([0, 0, 0, 0], 2, 0.0),
        ([-1, -2, -3, -4], 2, -1.5),
        ([-1, -2, -3, -4], 4, -2.5),
        ([1, 2, 3, 4, 5], 5, 3.0),
        ([4, 0, 4, 3, 3], 5, 2.8),
        ([7, 4, 5, 8, 8, 3, 9, 8, 7, 6], 7, 7.0),
        ([-10000, 10000], 1, 10000.0),
    ],
)
def test_find_max_average(nums, k, expected):
    assert Solution().findMaxAverage(nums, k) == pytest.approx(expected, abs=1e-5)


def test_matches_brute_force():
    nums = [3, -1, 4, -1, 5, -9, 2, 6, -5, 3, 5]
    for k in range(1, len(nums) + 1):
        brute = max(sum(nums[i:i + k]) / k for i in range(len(nums) - k + 1))
        assert Solution().findMaxAverage(nums, k) == pytest.approx(brute, abs=1e-5)


if __name__ == "__main__":
    pytest.main([__file__])
