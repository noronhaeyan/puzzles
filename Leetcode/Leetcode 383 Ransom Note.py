import random
from collections import Counter

import pytest


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomCounter = Counter(ransomNote)
        magazineCounter = Counter(magazine)

        for l in ransomCounter:
            if l not in magazineCounter:
                return False
            if ransomCounter[l] > magazineCounter[l]:
                return False

        return True


def brute_force(ransomNote, magazine):
    chars = list(magazine)
    for c in ransomNote:
        if c in chars:
            chars.remove(c)
        else:
            return False
    return True


@pytest.mark.parametrize(
    "ransomNote, magazine, expected",
    [
        ("a", "b", False),
        ("aa", "ab", False),
        ("aa", "aab", True),
        ("a", "a", True),
        ("abc", "cba", True),
        ("abc", "ab", False),
        ("a", "bbbbba", True),
        ("aab", "baa", True),
        ("aaa", "aa", False),
        ("z", "abcdefghijklmnopqrstuvwxy", False),
        ("a" * 100000, "a" * 100000, True),
        ("a" * 100000, "a" * 99999 + "b", False),
    ],
)
def test_can_construct(ransomNote, magazine, expected):
    assert Solution().canConstruct(ransomNote, magazine) is expected


def test_matches_brute_force_random():
    rng = random.Random(4)
    for _ in range(200):
        note = "".join(rng.choice("abc") for _ in range(rng.randint(1, 8)))
        mag = "".join(rng.choice("abc") for _ in range(rng.randint(1, 12)))
        assert Solution().canConstruct(note, mag) is brute_force(note, mag)


if __name__ == "__main__":
    pytest.main([__file__])
