def apply_discount(price, discount):
    return price * (1 - discount)


def checkout_total(prices, discount):
    discounted = [apply_discount(p, discount) for p in prices]
    return sum(discounted)
