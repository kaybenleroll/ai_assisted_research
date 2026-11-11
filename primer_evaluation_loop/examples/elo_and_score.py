"""Exercise the primer's Elo update and score-token expectation offline."""

import math


def elo_update(rating_a: float, rating_b: float,
               outcome: float, k_factor: float = 32) -> tuple[float, float]:
    expected_a = 1 / (1 + 10 ** ((rating_b - rating_a) / 400))
    expected_b = 1 - expected_a
    new_rating_a = rating_a + k_factor * (outcome - expected_a)
    new_rating_b = rating_b + k_factor * ((1 - outcome) - expected_b)
    return new_rating_a, new_rating_b


def g_eval_score(logprobs: dict[str, float]) -> float:
    total = sum(math.exp(lp) for lp in logprobs.values())
    p_scores = {token: math.exp(lp) / total for token, lp in logprobs.items()}
    return sum(int(token) * p for token, p in p_scores.items())


# Common K, complementary scores, and finite ratings; equal-rating draws do
# not move either rating. Unequal-rating draws generally do change ratings.
tol = 1e-10  # absolute tolerance for floating-point rating arithmetic
close = lambda a, b: math.isclose(a, b, rel_tol=0, abs_tol=tol)
assert elo_update(1500, 1500, 0.5) == (1500, 1500)
for rating_a, rating_b in [(1500, 1500), (1600, 1400)]:
    for outcome in (0.0, 0.5, 1.0):
        new_a, new_b = elo_update(rating_a, rating_b, outcome)
        assert close(new_a - rating_a, -(new_b - rating_b))
        assert close(new_a + new_b, rating_a + rating_b)
assert elo_update(1500, 1500, 1.0) == (1516, 1484)
assert elo_update(1600, 1400, 0.5)[0] < 1600

# Fixed positive token weights stand in for probabilities from one position;
# no model is called. Normalisation gives (1+4+9+16+25)/15 = 11/3.
weights = {str(i): float(i) for i in range(1, 6)}
score = g_eval_score({token: math.log(weight) for token, weight in weights.items()})
assert 1 <= score <= 5
assert close(score, 11 / 3)
assert close(g_eval_score({str(i): 0.0 for i in range(1, 6)}), 3.0)
print(f"Elo invariants hold; fixed score-token expectation: {score:.12f}")
