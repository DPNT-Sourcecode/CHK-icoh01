import pydantic
import structlog
from collections import Counter

logger = structlog.get_logger()

def turn_exception_into_minus_1():
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                logger.error(e)
                return -1
        return wrapper
    return decorator


class Offer(pydantic.BaseModel):
    requirements: dict[str, int]
    price: int

    def are_requirements_met(self, basket: dict[str, int]) -> bool:
        for product, required_quantity in self.requirements.items():
            if not basket.get(product) or basket[product] < required_quantity:
                return False
        return True

class CheckoutSolution:
    offers: list[Offer] = [
        Offer(requirements={"A": 3}, price=130),
        Offer(requirements={"A": 5}, price=200),
        Offer(requirements={"B": 2}, price=45),
        Offer(requirements={"E": 2, "B": 1}, price=80),
    ]

    products = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
        "E": 40,
    }

    def __init__(self):
        # "Offers involving multiple items always give a better discount than offers containing fewer items."
        # so sort offers by requirement count:
        self.offers = sorted(self.offers, key=lambda o: sum(o.requirements.values()), reverse=True)

    @turn_exception_into_minus_1()
    def checkout(self, skus: str) -> int:
        counts = self.get_validated_count(skus)
        return self.calculate_cost(counts)

    def get_validated_count(self, skus: str) -> dict[str, int]:
        if not isinstance(skus, str):
            raise ValueError("Invalid input type, expected str")
        counts = Counter([sku for sku in skus])
        if not all(self.products.get(k) for k in counts.keys()):
            raise ValueError("Invalid product, not in the catalogue")
        return counts

    def calculate_cost(self, counts: Counter) -> int:
        total_cost = 0
        for offer in self.offers:
            if not offer.are_requirements_met(counts):
                continue
            max_apply_count = min((counts[req] // req_count for req, req_count in offer.requirements.items()))
            if max_apply_count == 0:
                continue
            for req, req_count in offer.requirements.items():
                counts[req] -= req_count * max_apply_count
            total_cost += offer.price * max_apply_count

        for product, count in counts.items():
            total_cost += self.products[product] * count
        return total_cost

