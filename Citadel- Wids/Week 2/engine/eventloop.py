import heapq

class EventLoop:
    def __init__(self, engine):
        self.engine = engine
        self.time = 0
        self.queue = []
        self._seq = 0

    def push_event(self, timestamp, order):
        heapq.heappush(
            self.queue,
            (timestamp, self._seq, order)
        )
        self._seq += 1

    def execute(self):
        while self.queue:
            ts, _, order = heapq.heappop(self.queue)
            self.time = ts
            self.engine.process_order(order)