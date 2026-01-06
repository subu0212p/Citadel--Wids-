from engine.order_book import OrderBook

class MatchingEngine:
    def __init__(self, book):
        self.book = book
        self.trade_history = []

    def _log_trade(self, price, qty, buy_ord, sell_ord, time):
        self.trade_history.append({
            "price": price,
            "quantity": qty,
            "buy_order_id": buy_ord.order_id,
            "sell_order_id": sell_ord.order_id,
            "timestamp": time,
        })

    def process_order(self, order):
        if order.side == "BUY":
            self._handle_buy(order)
        elif order.side == "SELL":
            self._handle_sell(order)

    def _handle_buy(self, buy_order):
        while buy_order.quantity > 0:
            best_ask = self.book.get_best_ask()
            if best_ask is None:
                break

            if buy_order.order_type == "LIMIT" and buy_order.price < best_ask.price:
                break

            exec_qty = min(buy_order.quantity, best_ask.quantity)
            exec_price = best_ask.price

            self._log_trade(
                exec_price,
                exec_qty,
                buy_order,
                best_ask,
                buy_order.timestamp
            )

            buy_order.quantity -= exec_qty
            best_ask.quantity -= exec_qty

            if best_ask.quantity == 0:
                self.book.remove_best_ask()

        if buy_order.quantity > 0 and buy_order.order_type == "LIMIT":
            self.book.add_order(buy_order)

    def _handle_sell(self, sell_order):
        while sell_order.quantity > 0:
            best_bid = self.book.get_best_bid()
            if best_bid is None:
                break

            if sell_order.order_type == "LIMIT" and sell_order.price > best_bid.price:
                break

            exec_qty = min(sell_order.quantity, best_bid.quantity)
            exec_price = best_bid.price

            self._log_trade(
                exec_price,
                exec_qty,
                best_bid,
                sell_order,
                sell_order.timestamp
            )

            sell_order.quantity -= exec_qty
            best_bid.quantity -= exec_qty

            if best_bid.quantity == 0:
                self.book.remove_best_bid()

        if sell_order.quantity > 0 and sell_order.order_type == "LIMIT":
            self.book.add_order(sell_order)