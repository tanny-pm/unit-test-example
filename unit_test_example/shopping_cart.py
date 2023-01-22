class ShoppingCart:
    def __init__(self, max_size: int) -> None:
        self.items: list[str] = []
        self.max_size = max_size

    def add(self, item: str):
        if self.size() == self.max_size:
            raise OverflowError("cannot add more items")
        self.items.append(item)

    def size(self) -> int:
        return len(self.items)

    def get_items(self) -> list[str]:
        return self.items

    def get_total_price(self, price_map):
        total_pricee = 0
        for item in self.items:
            total_pricee += price_map.get(item)

        return total_pricee
