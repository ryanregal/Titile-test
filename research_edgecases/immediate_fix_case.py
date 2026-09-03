def is_positive(value):
    return value is not None and value > 0


def describe(value):
    return "positive" if is_positive(value) else "not positive"
