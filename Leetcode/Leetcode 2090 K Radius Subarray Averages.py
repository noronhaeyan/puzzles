import pytest


class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        temp = 0
        output = []
        for i in range(n):
            if i < k:
                output.append(-1)
            elif i > n - k - 1:
                output.append(-1)
            elif i == k:
                for j in range(2 * k + 1):
                    temp += nums[j]
                output.append(temp // (2 * k + 1))
            else:
                temp += nums[i + k]
                temp -= nums[i - k - 1]
                output.append(temp // (2 * k + 1))

        return output


def brute_force(nums, k):
    n = len(nums)
    return [
        sum(nums[i - k:i + k + 1]) // (2 * k + 1) if i - k >= 0 and i + k < n else -1
        for i in range(n)
    ]


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([7, 4, 3, 9, 1, 8, 5, 2, 6], 3, [-1, -1, -1, 5, 4, 4, -1, -1, -1]),
        ([100000], 0, [100000]),
        ([8], 100000, [-1]),
        ([1, 2, 3], 0, [1, 2, 3]),
        ([1, 2, 3], 1, [-1, 2, -1]),
        ([1, 2, 3], 2, [-1, -1, -1]),
        ([1, 2, 3, 4, 5], 2, [-1, -1, 3, -1, -1]),
        ([0, 0, 0, 0], 1, [-1, 0, 0, -1]),
        ([1, 1, 2], 1, [-1, 1, -1]),
        ([100000] * 5, 1, [-1, 100000, 100000, 100000, -1]),
    ],
)
def test_get_averages(nums, k, expected):
    assert Solution().getAverages(nums, k) == expected


def test_matches_brute_force():
    nums = [5, 0, 12, 7, 3, 9, 1, 4, 8, 2, 6]
    for k in range(0, len(nums) + 2):
        assert Solution().getAverages(nums, k) == brute_force(nums, k)


if __name__ == "__main__":
    pytest.main([__file__])
