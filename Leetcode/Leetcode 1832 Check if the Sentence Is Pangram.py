import string

import pytest


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        visited = set()

        for s in sentence:
            visited.add(s)

        return len(visited) == 26


@pytest.mark.parametrize(
    "sentence, expected",
    [
        ("thequickbrownfoxjumpsoverthelazydog", True),
        ("leetcode", False),
        ("a", False),
        (string.ascii_lowercase, True),
        (string.ascii_lowercase[::-1], True),
        (string.ascii_lowercase[:-1], False),
        (string.ascii_lowercase * 3, True),
        ("a" * 1000, False),
        (string.ascii_lowercase[1:] + "b" * 10, False),
        ("abcdefghijklmnopqrstuvwxyy", False),
    ],
)
def test_check_if_pangram(sentence, expected):
    assert Solution().checkIfPangram(sentence) is expected


def test_matches_set_superset():
    sentences = ["thequickbrownfoxjumpsoverthelazydog", "leetcode", "abc", "zyxwvutsrqponmlkjihgfedcba"]
    for sentence in sentences:
        expected = set(string.ascii_lowercase) <= set(sentence)
        assert Solution().checkIfPangram(sentence) is expected


if __name__ == "__main__":
    pytest.main([__file__])
