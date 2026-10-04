import random

import pytest


class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:

        visited = set()
        winners = {}
        losers = {}

        for match in matches:
            winners[match[0]] = winners.get(match[0], 0) + 1
            losers[match[1]] = losers.get(match[1], 0) + 1

        output1 = []
        output2 = []

        for winner in winners:
            if winner in losers:
                continue
            output1.append(winner)

        for loser in losers:
            if losers[loser] == 1:
                output2.append(loser)

        return [sorted(output1), sorted(output2)]


def brute_force(matches):
    players = {p for m in matches for p in m}
    loss = {p: 0 for p in players}
    for _, loser in matches:
        loss[loser] += 1
    return [
        sorted(p for p in players if loss[p] == 0),
        sorted(p for p in players if loss[p] == 1),
    ]


@pytest.mark.parametrize(
    "matches, expected",
    [
        (
            [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]],
            [[1, 2, 10], [4, 5, 7, 8]],
        ),
        ([[2, 3], [1, 3], [5, 4], [6, 4]], [[1, 2, 5, 6], []]),
        ([[1, 2]], [[1], [2]]),
        ([[1, 2], [2, 1]], [[], [1, 2]]),
        ([[1, 2], [1, 3], [1, 4]], [[1], [2, 3, 4]]),
        ([[1, 2], [3, 2]], [[1, 3], []]),
        ([[100000, 1]], [[100000], [1]]),
        ([[1, 2], [2, 3], [3, 1]], [[], [1, 2, 3]]),
    ],
)
def test_find_winners(matches, expected):
    assert Solution().findWinners(matches) == expected


def test_matches_brute_force_random():
    rng = random.Random(1)
    for _ in range(200):
        pairs = {
            (a, b)
            for a in range(1, 9)
            for b in range(1, 9)
            if a != b and rng.random() < 0.2
        }
        if not pairs:
            continue
        matches = [list(p) for p in pairs]
        rng.shuffle(matches)
        assert Solution().findWinners(matches) == brute_force(matches)


if __name__ == "__main__":
    pytest.main([__file__])
