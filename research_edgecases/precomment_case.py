def normalize_name(name):
    return name.strip().title()


def greet(name):
    cleaned = normalize_name(name)
    return f"Hello, {cleaned}"
