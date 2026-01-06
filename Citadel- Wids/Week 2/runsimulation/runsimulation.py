import random
from engine.order_book import OrderBook
from engine.matching_engine import MatchingEngine
from engine.event_loop import EventLoop
from agents.noise_agent import NoiseAgent
from analytics.tape import TradeTape
from analytics.snapshots import SnapshotRecorder
from analytics.metrics import vwap

random.seed(42)

book = OrderBook()
engine = MatchingEngine(book)
loop = EventLoop(engine)

tape = TradeTape()
snapshots = SnapshotRecorder()

agents = [NoiseAgent(uid=i) for i in range(10)]

current_time = 0

for _ in range(50):
    current_time += 1
    agent = random.choice(agents)
    order = agent.decide_action(current_time)
    if order is not None:
        loop.push_event(current_time, order)

loop.execute()

for trade in engine.trade_history:
    tape.add(trade)

print("VWAP:", vwap(tape.log))