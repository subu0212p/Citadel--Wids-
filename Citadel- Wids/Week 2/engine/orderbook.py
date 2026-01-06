import heapq

class OrderBook:
    def __init__(self):
        self.buy_heap = []
        self.sell_heap = []

    def add(self, order):
        if order.side == "BUY":
            heapq.heappush(
                self.buy_heap,
                (-order.price, order.timestamp, order)
            )
        elif order.side == "SELL":
            heapq.heappush(
                self.sell_heap,
                (order.price, order.timestamp, order)
            )

    def best_bid(self):
        if not self.buy_heap:
            return None
        return self.buy_heap[0][2]

    def best_ask(self):
        if not self.sell_heap:
            return None
        return self.sell_heap[0][2]

    def pop_best_bid(self):
        if self.buy_heap:
            heapq.heappop(self.buy_heap)

    def pop_best_ask(self):
        if self.sell_heap:
            heapq.heappop(self.sell_heap)