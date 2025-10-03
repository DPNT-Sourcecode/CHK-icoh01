from collections import Counter

products = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
}

offers = {
    "A": {"count": 3, "price": 130},
    "B": {"count": 2, "price": 45},
}

class CheckoutSolution:
    def checkout(self, skus: str) -> int:
        if not isinstance(skus, str):
            raise ValueError("Invalid input, SKUs must be a string")
        raw_skus = [sku for sku in skus]
        counts = Counter(raw_skus)
        total_cost = 0
        for sku, count in counts.items():
            if not products.get(sku):
                raise ValueError("Invalid product, SKU not found")

            if offer := offers.get(sku):
                if count > offer["count"]:
                    total_cost += offer["price"] * (count // offer["count"])
                    count -= count % offer["count"]
            if count:
                total_cost += count * products[sku]




