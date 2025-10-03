import pydantic
from collections import Counter


class Product(pydantic.BaseModel):
    name: str
    price: int


class Offer(pydantic.BaseModel):
    requirements: dict[str, int]
    price: int


class CheckoutSolution:
    offers: list[Offer] = [
        Offer(requirements={"A": 3}, price=130),
        Offer(requirements={"A": 5}, price=200),
        Offer(requirements={"B": 2}, price=45),
        Offer(requirements={"E": 2, "B": -1}, price=80),
    ]

    products = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
        "E": 40,
    }

    def checkout(self, skus: str) -> int:
        if not isinstance(skus, str):
            return -1
        counts = Counter([sku for sku in skus])
        return self.calculate_cost(counts)

    def calculate_cost(self, counts: Counter) -> int:
        total_cost = 0
        for offer in self.offers:
            # get applicable offers
            # minimise for cost
            ...
        for sku, count in counts.items():
            #
            if not self.products.get(sku):
                return -1

            if offer := self.offers.get(sku):
                if count >= offer["count"]:
                    total_cost += offer["price"] * (count // offer["count"])
                    count = count % offer["count"]
            if count:
                total_cost += count * self.products[sku]

        return total_cost

def is_applicable(offer: Offer, counts: Counter) -> bool:
    required_items = offer[0]
