from engine.order import Order

class MarketMakerAgent:
    def __init__(self, uid, spread_width=1, size=5):
        self.uid = uid
        self.spread_width = spread_width
        self.order_size = size

    def generate_orders(self, reference_price, timestamp):
        if reference_price is None:
            return []

        buy_order = Order(
            self.uid,
            "BUY",
            reference_price - self.spread_width,
            self.order_size,
            timestamp,
            "LIMIT"
        )

        sell_order = Order(
            self.uid,
            "SELL",
            reference_price + self.spread_width,
            self.order_size,
            timestamp,
            "LIMIT"
        )

        return [buy_order, sell_order]