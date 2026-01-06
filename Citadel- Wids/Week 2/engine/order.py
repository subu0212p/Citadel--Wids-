class Order:
    def __init__(self, oid, side, price, qty, timestamp, kind):
        self.order_id = oid
        self.side = side
        self.price = price
        self.quantity = qty
        self.timestamp = timestamp
        self.order_type = kind

    def __repr__(self):
        return (
            f"Order("
            f"id={self.order_id}, "
            f"side={self.side}, "
            f"price={self.price}, "
            f"qty={self.quantity}, "
            f"ts={self.timestamp}, "
            f"type={self.order_type}"
            f")"
        )