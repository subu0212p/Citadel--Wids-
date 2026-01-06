import random
from engine.order import Order

class NoiseAgent:
    def __init__(self, uid, max_size=10):
        self.uid = uid
        self.max_size = max_size

    def decide_action(self, timestamp):
        direction = random.choice(["BUY", "SELL"])
        qty = random.randint(1, self.max_size)

        return Order(
            self.uid,
            direction,
            None,
            qty,
            timestamp,
            "MARKET"
        )