from engine.order import Order
from engine.order_book import OrderBook
from engine.matching_engine import MatchingEngine

book = OrderBook()
engine = MatchingEngine(book)

# Insert SELL limit orders (ask ladder)
engine.process_order(Order(1, "SELL", 101, 10, 1, "LIMIT"))
engine.process_order(Order(2, "SELL", 102, 20, 2, "LIMIT"))
engine.process_order(Order(3, "SELL", 103, 30, 3, "LIMIT"))

# MARKET BUY order that should consume all asks
engine.process_order(Order(4, "BUY", None, 60, 4, "MARKET"))

print("Executed Trades:")
for trade in engine.trade_history:
    print(trade)

print("Remaining best ask:", book.best_ask())