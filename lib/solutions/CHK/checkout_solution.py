products = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
}

class CheckoutSolution:
    def checkout(self, skus: str):
        if not isinstance(skus, str):
            raise ValueError("Invalid input, SKUs must be a string")
        raw_skus = [sku for sku in skus]




