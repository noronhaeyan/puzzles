import random

import pytest


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        visited = set(jewels)

        output = 0
        for s in stones:
            if s in visited:
                output += 1

        return output


@pytest.mark.parametrize(
    "jewels, stones, expected",
    [
        ("aA", "aAAbbbb", 3),
        ("z", "ZZ", 0),
        ("a", "a", 1),
        ("a", "b", 0),
        ("a", "A", 0),
        ("abc", "abcabc", 6),
        ("abc", "xyz", 0),
        ("a", "a" * 50, 50),
        ("aA", "AaAaAa", 6),
        ("xyz", "aXbYcZ", 0),
        ("b", "abababab", 4),
    ],
)
def test_num_jewels_in_stones(jewels, stones, expected):
    assert Solution().numJewelsInStones(jewels, stones) == expected


def test_matches_brute_force_random():
    rng = random.Random(5)
    letters = "abcABC"
    for _ in range(200):
        jewels = "".join(rng.sample(letters, rng.randint(1, 4)))
        stones = "".join(rng.choice(letters) for _ in range(rng.randint(1, 20)))
        expected = sum(stones.count(j) for j in jewels)
        assert Solution().numJewelsInStones(jewels, stones) == expected


if __name__ == "__main__":
    pytest.main([__file__])
