"""Check the primer's deterministic, fully penalised logistic regression."""

from math import exp, hypot, isfinite, log1p, sqrt


LAMBDA = 0.1


def observation(i):
    x1 = (((37 * i + 11) % 101) - 50) / 15.0
    x2 = (((53 * i + 7) % 97) - 48) / 15.0
    noise = (((29 * i + 3) % 19) - 9) / 4.0
    return x1, x2, int(0.3 + 1.2 * x1 - 0.9 * x2 + noise >= 0.0)


raw = [observation(i) for i in range(72)]
train, validation = raw[:48], raw[48:]
means = tuple(sum(row[j] for row in train) / len(train) for j in (0, 1))
scales = tuple(
    sqrt(sum((row[j] - means[j]) ** 2 for row in train) / len(train))
    for j in (0, 1)
)
assert all(scale > 0 for scale in scales), "training features must have variance"


def prepare(rows):
    features = [
        (1.0, (row[0] - means[0]) / scales[0], (row[1] - means[1]) / scales[1])
        for row in rows
    ]
    return features, [row[2] for row in rows]


x_train, y_train = prepare(train)
x_validation, y_validation = prepare(validation)


def dot(a, b):
    return sum(left * right for left, right in zip(a, b))


def softplus(score):
    return max(score, 0.0) + log1p(exp(-abs(score)))


def sigmoid(score):
    if score >= 0:
        return 1.0 / (1.0 + exp(-score))
    value = exp(score)
    return value / (1.0 + value)


def objective_gradient(theta, x=x_train, y=y_train):
    scores = [dot(row, theta) for row in x]
    probabilities = [sigmoid(score) for score in scores]
    data_loss = sum(
        softplus(score) - target * score
        for score, target in zip(scores, y)
    ) / len(y)
    gradient = tuple(
        sum((probability - target) * row[j]
            for probability, target, row in zip(probabilities, y, x)) / len(y)
        + LAMBDA * theta[j]
        for j in range(3)
    )
    return data_loss + 0.5 * LAMBDA * dot(theta, theta), gradient


probe = (0.2, -0.3, 0.4)
direction = (0.5, -0.4, sqrt(0.59))
h = 1e-6
plus = tuple(value + h * delta for value, delta in zip(probe, direction))
minus = tuple(value - h * delta for value, delta in zip(probe, direction))
finite_difference = (objective_gradient(plus)[0] - objective_gradient(minus)[0]) / (2 * h)
analytic = dot(objective_gradient(probe)[1], direction)
assert abs(finite_difference - analytic) < 1e-8, "logistic gradient mismatch"

original_value, original_gradient = objective_gradient(probe)
reversed_value, reversed_gradient = objective_gradient(
    probe, tuple(reversed(x_train)), tuple(reversed(y_train))
)
assert abs(original_value - reversed_value) < 1e-14, "row order changed objective"
assert max(abs(a - b) for a, b in zip(original_gradient, reversed_gradient)) < 1e-14, (
    "row order changed gradient"
)
assert softplus(1000.0) == 1000.0 and softplus(-1000.0) >= 0.0, (
    "softplus is unstable at extreme scores"
)

smoothness_bound = sum(dot(row, row) for row in x_train) / (4 * len(x_train)) + LAMBDA
step_size = 1 / smoothness_bound
theta = (0.0, 0.0, 0.0)
initial_value, _ = objective_gradient(theta)
for _ in range(60):
    value, gradient = objective_gradient(theta)
    theta = tuple(coef - step_size * grad for coef, grad in zip(theta, gradient))
    next_value, _ = objective_gradient(theta)
    assert isfinite(next_value), "non-finite training objective"
    assert next_value <= value + 1e-14, "training objective increased"

final_value, final_gradient = objective_gradient(theta)
assert final_value < initial_value - 0.1, "fit did not materially improve"
assert hypot(*final_gradient) < 1e-8, "fit did not reach a small gradient"
validation_value, _ = objective_gradient(theta, x_validation, y_validation)
assert isfinite(validation_value), "non-finite held-out objective"
print(f"logistic objective: {initial_value:.6f} -> {final_value:.6f}; "
      f"gradient norm: {hypot(*final_gradient):.3e}")
