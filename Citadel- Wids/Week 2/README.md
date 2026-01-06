# Agent-Based Market Simulation (Week 2)

This project implements a simple agent-based financial market simulator.  
It models how different trading agents interact with a central exchange using
an order book and matching engine.

## Components

### Agents
- **NoiseAgent**: Places random market buy/sell orders.
- (Extensible) Agents decide actions based on market information.

### Engine
- **OrderBook**: Maintains bid and ask queues using priority heaps.
- **MatchingEngine**: Matches incoming orders and records executed trades.
- **EventLoop**: Schedules and processes orders in time order.

### Analytics
- **TradeTape**: Stores executed trades.
- **SnapshotRecorder**: Records market snapshots such as best bid/ask.
- **Metrics**:
  - VWAP (Volume Weighted Average Price)
  - Average spread
  - Volatility (log-return based)

## Running the Simulation

Run:
```bash
python run_simulation.py