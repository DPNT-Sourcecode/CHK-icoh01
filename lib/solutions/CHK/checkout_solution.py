import pydantic
from collections import Counter


class Offer(pydantic.BaseModel):
    requirements: dict[str, int]
    price: int

    def are_requirements_met(self, basket: dict[str, int]) -> bool:
        for product, required_quantity in self.requirements.values():
            if not basket.get(product) or basket[product] < required_quantity:
                return False
        return True

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
        offers_in_play = []
        for offer in self.offers:
            if offer.are_requirements_met(counts):
                offers_in_play.append(offer)
            # get applicable offers
            # minimise for cost
            # calculate price of remaining items
            ...

        return total_cost

def is_applicable(offer: Offer, counts: Counter) -> bool:
    required_items = offer[0]


