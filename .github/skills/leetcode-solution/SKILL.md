---
name: leetcode-solution
description: Turn a copy-pasted LeetCode problem and solution into a pytest-style Python file in the Leetcode/ folder, run the tests, then commit and push to main. Use when the user pastes a LeetCode problem statement with Python code.
---

# LeetCode Solution Skill

The user pastes a LeetCode problem (statement, examples, constraints) together with their Python solution. Turn it into a tested file, then commit and push.

## Input

The paste is messy: the page text is run together, HTML entities appear (`&lt;`, `&gt;`), and the code has line numbers glued to each line (e.g. `1class Solution:2    def f(...)`). Reconstruct the code with correct indentation and remove the line numbers. If the pasted code is ambiguous, ask the user.

## Steps

1. **Identify the problem number and name.** The paste usually has no number. Determine it from the title (LeetCode problem number). State the number you chose in your reply.
2. **Create the file** in `Leetcode/` named `Leetcode <number> <Problem Name>.py`, for example `Leetcode 977 Squares of a Sorted Array.py`. Use the problem title as given, with punctuation that is unsafe in file names removed.
3. **File contents**, in this order:
   - `import pytest` (plus `random`, `Counter`, etc. only if used).
   - The user's `class Solution` copied faithfully. Keep their logic and variable names. Only make these changes:
     - use `list[int]` rather than `List[int]` so no `typing` import is needed;
     - remove debug `print` calls so test output stays clean.
     Mention any such change to the user.
   - A `brute_force` helper when a simple reference implementation exists.
   - `@pytest.mark.parametrize` tests covering: every example from the problem, the minimum-size input, boundary values from the constraints, all-same or all-empty cases, and tricky cases specific to the algorithm.
   - A randomized test against `brute_force` using a seeded `random.Random(n)`, around 200 iterations of small inputs, when a brute force exists.
   - A large-input test at the upper constraint when it is cheap.
   - End with:
     ```python
     if __name__ == "__main__":
         pytest.main([__file__])
     ```
   - Use `is` for bool results and `pytest.approx(..., abs=1e-5)` for floats.
   - Only add comments that need clarification.
4. **Run the tests**: `cd Leetcode && python -m pytest -q "<file>"`. If pytest is missing, `pip install pytest`. If a test fails, work out whether the expected value in the test or the user's solution is wrong. Fix wrong expectations in the test. If the user's solution is genuinely wrong, tell them instead of silently changing it.
5. **Commit and push** once the tests pass and the user has asked for it, or when this skill was invoked with commit and push requested:
   ```bash
   git add Leetcode/*.py
   git commit -m "Add Leetcode <numbers> solution(s) with tests" -m "Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>"
   git fetch origin
   git push origin HEAD:main
   ```
   The repo owner pushes straight to `main`. If `main` has moved and the push is not a fast-forward, rebase onto `origin/main` first. Never force push.
6. **Reply concisely**: the problem number you used, a link to the file, the test count and result, and the push result. Mention if the solution uses more space than the problem's follow-up asks for.

## Multiple problems in one session

The user may paste problems one after another and say "commit and push" only at the end. Create and test each file as it arrives, and batch the commit and push when asked.

## Do not

- Edit or commit the existing `.ipynb` notebooks.
- Commit unrelated files; stage only `Leetcode/*.py`.
- Change the user's algorithm without telling them.
