def clamp(value, low, high):
    return max(low, min(value, high))


def score(values):
    return sum(clamp(v, 0, 10) for v in values)
