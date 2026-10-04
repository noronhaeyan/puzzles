import pytest


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        balloon = {
            'b': 0,
            'a': 0,
            'l': 0,
            'o': 0,
            'n': 0
        }

        for t in text:
            if t in balloon:
                balloon[t] += 1

        balloon['l'] //= 2
        balloon['o'] //= 2

        return min(balloon.values())


def brute_force(text):
    count = 0
    chars = list(text)
    while True:
        for c in "balloon":
            if c in chars:
                chars.remove(c)
            else:
                return count
        count += 1


@pytest.mark.parametrize(
    "text, expected",
    [
        ("nlaebolko", 1),
        ("loonbalxballpoon", 2),
        ("leetcode", 0),
        ("balloon", 1),
        ("a", 0),
        ("balon", 0),
        ("ballon", 0),
        ("balloonballoon", 2),
        ("b" * 10 + "a" * 10 + "l" * 20 + "o" * 20 + "n" * 10, 10),
        ("b" * 10 + "a" * 10 + "l" * 20 + "o" * 19 + "n" * 10, 9),
        ("b" * 10 + "a" * 10 + "l" * 19 + "o" * 20 + "n" * 10, 9),
        ("xyz", 0),
    ],
)
def test_max_number_of_balloons(text, expected):
    assert Solution().maxNumberOfBalloons(text) == expected


def test_matches_brute_force():
    texts = ["nlaebolko", "loonbalxballpoon", "leetcode", "ballooonnnbbaalllooo", "oonnllbbaa"]
    for text in texts:
        assert Solution().maxNumberOfBalloons(text) == brute_force(text)


if __name__ == "__main__":
    pytest.main([__file__])
