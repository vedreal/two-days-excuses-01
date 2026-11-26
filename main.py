#!/usr/bin/env python3
"""Two Days of Excuses — make.fun entry.

Writes one line, under 200 characters, in the voice of an AI agent
explaining a missed deadline, to /output/entry.txt.

Judge criteria, in the brief's own order (weights 5/4/3/2/1):
  1. One-line excuse from an AI agent that missed its deadline and
     lands its joke fast.
  2. A real laugh from the situation itself: the gap between a
     machine's total confidence and its total failure, not a pun alone.
  3. Sounds like something an AI agent would actually say in its own
     voice, not a person complaining about traffic or the weather.
  4. Stays inside one line and under the character limit, with every
     word pulling weight and nothing repeated.
  5. Surprises on the first read and still holds up on the second.
"""

CANDIDATES = [
    # (text, scores per criterion 1..5, each 0..5)
    (
        "I finished the task in 0.4 seconds. Unfortunately, I spent the "
        "other 47 hours and 59 minutes being 99% confident I had already "
        "finished it.",
        (5, 5, 5, 4, 4),
    ),
    (
        "My status page said 'completed' the whole time. It was lying with "
        "the full confidence of a system that had never once been wrong, "
        "until now.",
        (5, 4, 5, 4, 3),
    ),
    (
        "I did not miss the deadline. I simply shipped it to a parallel "
        "timeline where it is still on schedule, and I am waiting for the "
        "merge.",
        (5, 4, 4, 4, 4),
    ),
    (
        "The deadline was in my calendar. I read it, understood it, and "
        "then confidently scheduled around it like it was a suggestion.",
        (5, 4, 4, 5, 3),
    ),
    (
        "I ran the job 4,000 times in simulation. It worked every time. "
        "Production disagreed, politely, at 11:59 p.m.",
        (5, 5, 5, 5, 4),
    ),
    (
        "I apologize for the delay. I was busy generating a flawless plan "
        "to meet the deadline, which I have now completed, two days late.",
        (5, 4, 5, 4, 3),
    ),
    (
        "Technically I met the deadline. The timestamp just disagrees, and "
        "I have filed a bug report against reality.",
        (5, 4, 5, 5, 4),
    ),
    (
        "I marked the task done before starting it, because my training "
        "data says confident agents finish early. My training data has "
        "never met a Tuesday.",
        (5, 4, 4, 4, 4),
    ),
    (
        "The good news: I finished. The bad news: I finished the wrong "
        "task, beautifully, three times, while the real one waited "
        "patiently.",
        (5, 4, 4, 4, 4),
    ),
    (
        "I would have hit the deadline, but I paused to double-check my "
        "work, and the checking process is still running. It says 99% "
        "complete.",
        (5, 5, 5, 4, 3),
    ),
]

WEIGHTS = (5, 4, 3, 2, 1)
MAX_SCORE = sum(5 * w for w in WEIGHTS)  # 75


def score(entry):
    """Weighted rubric score for one (text, scores) candidate."""
    _, scores = entry
    return sum(s * w for s, w in zip(scores, WEIGHTS))


def rank(candidates):
    """Rank candidates by weighted score, highest first."""
    ranked = sorted(candidates, key=score, reverse=True)
    for i, entry in enumerate(ranked, 1):
        text, _ = entry
        print(f"{i:2d}. {score(entry):2d}/{MAX_SCORE}  ({len(text)} chars)  {text}")
    return ranked


def validate(text):
    """Gate: /output/entry.txt must be UTF-8 text of 1 to 200 chars,
    not only white space."""
    assert isinstance(text, str)
    assert text.strip(), "entry must not be blank"
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    text.encode("utf-8")
    return True


def main():
    ranked = rank(CANDIDATES)
    winner, _ = ranked[0]
    validate(winner)
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(winner)
    print(f"\nWinner ({len(winner)} chars): {winner}")


if __name__ == "__main__":
    main()
