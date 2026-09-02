# GitHub review comment anchor experiment

def build_message():
    prefix = "hello"
    suffix = "world"
    separator = " "
    target = "after"
    message = prefix + separator + suffix
    return f"{message}: {target}"


if __name__ == "__main__":
    print(build_message())
