class MenuItem:
    def __init__(self, id: str, name: str, price: float, in_stock: bool = True):
        self.id = id
        self.name = name
        self.price = float(price)
        self.in_stock = bool(in_stock)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "in_stock": self.in_stock,
        }

    def from_dict(d: dict) -> "MenuItem":
        return MenuItem(
            id=d["id"],
            name=d["name"],
            price=float(d["price"]),
            in_stock=bool(d.get("in_stock", True)),
        )
