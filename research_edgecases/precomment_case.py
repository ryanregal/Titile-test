def normalize_name(name):
    return name.strip()


def greet(name):
    return f"Hello, {normalize_name(name)}"
