from collections import Counter

type Offer = tuple[dict[str, int], int]

offers: list[Offer] = [
    ({"A": 3}, 130),
    ({"A": 5}, 200),
    ({"B": 2}, 45),
    ({"E": 2, "B": -1}, 80),
]

products = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
}


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

def find_offer(offers, product) list[Offer]:


class CheckoutSolution:
    def checkout(self, skus: str) -> int:
        if not isinstance(skus, str):
            return -1
        counts = Counter([sku for sku in skus])
        return calculate_cost(counts)



