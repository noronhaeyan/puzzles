import random

import pytest


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        output = 0
        left = 0
        for right in range(len(s)):
            if s[right] in visited:
                while s[right] in visited:
                    visited.remove(s[left])
                    left += 1

            visited.add(s[right])
            output = max(output, right - left + 1)

        return output


def brute_force(s):
    best = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            sub = s[i:j + 1]
            if len(set(sub)) == len(sub):
                best = max(best, len(sub))
    return best


@pytest.mark.parametrize(
    "s, expected",
    [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        ("a", 1),
        ("ab", 2),
        ("aab", 2),
        ("abba", 2),
        ("dvdf", 3),
        ("tmmzuxt", 5),
        (" ", 1),
        ("a b a", 3),
        ("abcdefghijklmnopqrstuvwxyz", 26),
        ("1234!@#$1", 8),
    ],
)
def test_length_of_longest_substring(s, expected):
    assert Solution().lengthOfLongestSubstring(s) == expected


def test_matches_brute_force_random():
    rng = random.Random(6)
    for _ in range(200):
        s = "".join(rng.choice("abcd") for _ in range(rng.randint(0, 20)))
        assert Solution().lengthOfLongestSubstring(s) == brute_force(s)


def test_large_input():
    assert Solution().lengthOfLongestSubstring("ab" * 50000) == 2


if __name__ == "__main__":
    pytest.main([__file__])
