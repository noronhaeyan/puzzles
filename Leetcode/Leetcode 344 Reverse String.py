import pytest


class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        i = 0
        j = n - 1
        while i < j:
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            i += 1
            j -= 1


@pytest.mark.parametrize(
    "s, expected",
    [
        (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
        (["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"]),
        (["a"], ["a"]),
        (["a", "b"], ["b", "a"]),
        (["a", "b", "c"], ["c", "b", "a"]),
        (["a", "a", "a"], ["a", "a", "a"]),
        ([" ", "!", "~"], ["~", "!", " "]),
    ],
)
def test_reverse_string(s, expected):
    result = Solution().reverseString(s)
    assert result is None
    assert s == expected


def test_modifies_in_place():
    s = list("abcdef")
    original_id = id(s)
    Solution().reverseString(s)
    assert id(s) == original_id
    assert s == list("fedcba")


def test_large_input():
    s = [chr(97 + i % 26) for i in range(10**5)]
    expected = s[::-1]
    Solution().reverseString(s)
    assert s == expected


if __name__ == "__main__":
    pytest.main([__file__])
