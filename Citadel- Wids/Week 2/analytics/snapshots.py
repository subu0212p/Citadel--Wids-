class SnapshotRecorder:
    def __init__(self):
        self.data = []

    def capture(self, timestamp, top_bid, top_ask):
        if top_bid is not None and top_ask is not None:
            mid = (top_bid.price + top_ask.price) / 2
            spread_val = top_ask.price - top_bid.price
        else:
            mid = None
            spread_val = None

        self.data.append({
            "timestamp": timestamp,
            "best_bid": top_bid.price if top_bid else None,
            "best_ask": top_ask.price if top_ask else None,
            "mid_price": mid,
            "spread": spread_val,
        })