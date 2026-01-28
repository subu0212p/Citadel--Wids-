import numpy as np


class MarketEnv:
    """
    Minimal continuous double-auction market with
    order-flow-based price impact.

    This environment:
    - Maintains a limit order book
    - Executes market orders
    - Applies price impact once per timestep
    - Logs full market state for analysis
    """

    def __init__(self, init_price=1.0, tick_size=0.01, impact_strength=0.001):
        self.tick_size = tick_size
        self.mid_price = init_price
        self.impact_strength = impact_strength

        # Order book: price -> volume
        self.bids = {}
        self.asks = {}

        # Logs
        self.trade_log = []
        self.book_log = []
        self.mid_price_log = []

        # Order-flow tracking (reset every timestep)
        self.buy_volume = 0.0
        self.sell_volume = 0.0

    # --------------------------------------------------
    # Order book utilities
    # --------------------------------------------------
    def best_bid(self):
        return max(self.bids.keys()) if self.bids else None

    def best_ask(self):
        return min(self.asks.keys()) if self.asks else None

    # --------------------------------------------------
    # Order processing
    # --------------------------------------------------
    def process_order(self, order, time_step):
        """
        Process a single order dictionary.
        """
        side = order["side"]
        volume = order["volume"]
        agent_id = order["agent_id"]
        order_type = order["type"]

        if order_type == "market":
            self._execute_market_order(side, volume, agent_id, time_step)

        elif order_type == "limit":
            price = order["price"]
            self._add_limit_order(side, price, volume)

    def _execute_market_order(self, side, volume, agent_id, time_step):
        """
        Execute against the opposite side of the book.
        """
        book = self.asks if side == "buy" else self.bids

        # Track order flow for price impact
        if side == "buy":
            self.buy_volume += volume
        else:
            self.sell_volume += volume

        while volume > 0 and book:
            best_price = min(book) if side == "buy" else max(book)
            trade_volume = min(volume, book[best_price])

            # Log trade
            self.trade_log.append({
                "time": time_step,
                "price": best_price,
                "volume": trade_volume,
                "agent_id": agent_id,
                "side": side
            })

            book[best_price] -= trade_volume
            volume -= trade_volume

            if book[best_price] == 0:
                del book[best_price]

    def _add_limit_order(self, side, price, volume):
        """
        Add a limit order to the book.
        """
        book = self.bids if side == "buy" else self.asks
        book[price] = book.get(price, 0.0) + volume

    # --------------------------------------------------
    # Market update (call ONCE per timestep)
    # --------------------------------------------------
    def update_market(self):
        """
        Apply order-flow-based price impact.
        Must be called once per timestep AFTER all agents act.
        """
        imbalance = self.buy_volume - self.sell_volume
        self.mid_price += self.impact_strength * imbalance

        # Enforce strictly positive price
        self.mid_price = max(self.tick_size, self.mid_price)

        # Reset flow counters
        self.buy_volume = 0.0
        self.sell_volume = 0.0

    # --------------------------------------------------
    # Logging
    # --------------------------------------------------
    def log_state(self, time_step):
        """
        Log order book snapshot and mid-price.
        """
        for price in set(self.bids.keys()).union(self.asks.keys()):
            self.book_log.append({
                "time": time_step,
                "price_level": price,
                "bid_volume": self.bids.get(price, 0.0),
                "ask_volume": self.asks.get(price, 0.0)
            })

        spread = None
        if self.best_bid() is not None and self.best_ask() is not None:
            spread = self.best_ask() - self.best_bid()

        self.mid_price_log.append({
            "time": time_step,
            "mid_price": self.mid_price,
            "spread": spread
        })
