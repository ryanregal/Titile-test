def calculate_total(values):
    total = 0
    for value in values:
        total += value
    return total


def format_total(values):
    result = calculate_total(values)
    return f"Total: {result}"
