from collections import Counter

products = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
}

offers = [
    ({"A": 1}, 50),
    ({"A": 3}, 130),
    ({"A": 5}, 200),
    ({"B": 1}, 30),
    ({"B": 2}, 45),
    ({"C": 1}, 20),
    ({"D": 1}, 15),
    ({"E": 1}, 40),
    ({"E": 2, "B": -1}, 45),
]


def calculate_cost(counts: Counter) -> int:
    total_cost = 0
    for sku, count in counts.items():
        if not products.get(sku):
            return -1

        if offer := offers.get(sku):
            if count >= offer["count"]:
                total_cost += offer["price"] * (count // offer["count"])
                count = count % offer["count"]
        if count:
            total_cost += count * products[sku]

    return total_cost


class CheckoutSolution:
    def checkout(self, skus: str) -> int:
        if not isinstance(skus, str):
            return -1
        counts = Counter([sku for sku in skus])
        return calculate_cost(counts)

