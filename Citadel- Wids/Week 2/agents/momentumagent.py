from collections import deque
from engine.order import Order

class MomentumAgent:
    def __init__(self, uid, lookback=5, size=5):
        self.uid = uid
        self.lookback = lookback
        self.order_size = size
        self.recent_prices = deque(maxlen=lookback)

    def update_price(self, price):
        if price is not None:
            self.recent_prices.append(price)

    def decide_action(self, timestamp):
        if len(self.recent_prices) < self.lookback:
            return None

        avg_price = sum(self.recent_prices) / len(self.recent_prices)

        if self.recent_prices[-1] > avg_price:
            return Order(self.uid, "BUY", None, self.order_size, timestamp, "MARKET")
        else:
            return Order(self.uid, "SELL", None, self.order_size, timestamp, "MARKET")