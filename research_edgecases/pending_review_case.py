def apply_discount(price, discount):
    return price * (1 - discount)


def checkout_total(prices, discount):
    return sum(apply_discount(p, discount) for p in prices)
