import abc

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


class CheckoutSolution:
    @turn_exception_into_minus_1()
    def checkout(self, skus: str) -> int:
        return Pricer(catalogue=r4_catalogue).checkout(skus)


class Offer(pydantic.BaseModel):
    requirements: dict[str, int]
    price: int


class Group(pydantic.BaseModel):
    requirements: list[str]
    count: int
    price: int


class Catalogue(pydantic.BaseModel):
    groups: list[Group]
    offers: list[Offer]
    products: dict[str, int]


class Pricer:
    def __init__(self, catalogue: Catalogue) -> None:
        # "Offers involving multiple items always give a better discount than offers containing fewer items."
        # so sort offers by requirement count:
        self.offers = sorted(
            catalogue.offers, key=lambda o: sum(o.requirements.values()), reverse=True
        )
        self.products = catalogue.products
        self.groups = catalogue.groups

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

    def _handle_products(self, counts: dict[str, int]) -> int:
        total_cost = 0

        for product, count in counts.items():
            total_cost += self.products[product] * count
        return total_cost

    def _handle_offers(self, counts: dict[str, int]) -> int:
        total_cost = 0

        for offer in self.offers:
            apply_count = min(
                (
                    counts[req] // req_count
                    for req, req_count in offer.requirements.items()
                )
            )
            if apply_count == 0:
                continue
            for req, req_count in offer.requirements.items():
                counts[req] -= req_count * apply_count
            total_cost += offer.price * apply_count
        return total_cost

    def _handle_groups(self, counts: dict[str, int]) -> int:
        total_cost = 0

        for group in self.groups:
            apply_count = (
                sum(counts.get(req, 0) for req in self.requirements) // group.count
            )
            if apply_count == 0:
                continue

        return total_cost

    def calculate_cost(self, counts: dict[str, int]) -> int:
        total_cost = 0
        total_cost += self._handle_offers(counts)
        total_cost += self._handle_groups(counts)
        total_cost += self._handle_products(counts)
        return total_cost


r4_catalogue = Catalogue(
    groups=[
        Group(requirements=["S", "T", "X", "Y", "Z"], count=3, price=45),
    ],
    offers=[
        Offer(requirements={"A": 3}, price=130),
        Offer(requirements={"A": 5}, price=200),
        Offer(requirements={"B": 2}, price=45),
        Offer(requirements={"E": 2, "B": 1}, price=80),
        Offer(requirements={"F": 3}, price=20),
        Offer(requirements={"H": 5}, price=45),
        Offer(requirements={"H": 10}, price=80),
        Offer(requirements={"K": 2}, price=150),
        Offer(requirements={"N": 3, "M": 1}, price=120),
        Offer(requirements={"P": 5}, price=200),
        Offer(requirements={"Q": 3}, price=80),
        Offer(requirements={"R": 3, "Q": 1}, price=150),
        Offer(requirements={"U": 4}, price=120),
        Offer(requirements={"V": 2}, price=90),
        Offer(requirements={"V": 3}, price=130),
    ],
    products={
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
        "E": 40,
        "F": 10,
        "G": 20,
        "H": 10,
        "I": 35,
        "J": 60,
        "K": 70,
        "L": 90,
        "M": 15,
        "N": 40,
        "O": 10,
        "P": 50,
        "Q": 30,
        "R": 50,
        "S": 20,
        "T": 20,
        "U": 40,
        "V": 50,
        "W": 20,
        "X": 17,
        "Y": 20,
        "Z": 21,
    },
)




