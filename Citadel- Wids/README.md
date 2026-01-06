# Citadel × WiDS – Agent-Based Market Simulation Project

This repository documents a three-week learning and implementation project focused on
financial markets, randomness, and market microstructure.  
The project progresses from foundational concepts to a complete agent-based exchange
simulation with analytics.

---

## Week 0: Foundations – Python, Randomness, and Risk

### Work Done
- Revised Python fundamentals relevant for quantitative finance
- Implemented **Geometric Brownian Motion (GBM)** to model asset price evolution
- Simulated multiple GBM price paths with identical parameters
- Visualized:
  - Price paths over time
  - Histogram of final prices
- Wrote a short reflection on randomness and financial risk

### Key Concepts Learned
- Randomness plays a central role in financial markets
- Even with fixed drift and volatility, realized price paths vary significantly
- Risk is better understood as a **distribution of outcomes**, not a single forecast
- Volatility controls dispersion and uncertainty
- Losses are inherent possibilities, not anomalies

---

## Week 1: Market Microstructure & System Design

### Work Done
- Studied the architecture of a modern electronic market
- Designed a modular **market simulator architecture**
- Defined roles and interactions between:
  - Agents
  - Market environment
  - Order book
  - Trade logging and visualization

### Architecture Overview
- **Agents**
  - Observe market state
  - Decide actions
  - Submit orders
- **Market Environment**
  - Maintains simulation clock
  - Routes orders
  - Tracks market state
- **Order Book**
  - Maintains bids and asks
  - Price–time (FIFO) priority
  - Matching logic
- **Trade Logger & Analytics**
  - Records executed trades
  - Enables spread, depth, and tape visualization

### Key Concepts Learned
- Market microstructure fundamentals
- Price–time priority and FIFO matching
- Difference between liquidity providers and takers
- Role of randomness in order arrivals
- Separation of concerns in system design

---

## Week 2: Agent-Based Exchange Implementation

### Work Done
Implemented a complete working exchange simulator in Python:

#### Agents
- **NoiseAgent**
  - Submits random market orders
- **MomentumAgent**
  - Trades based on recent price trends
- **MarketMakerAgent**
  - Posts two-sided limit quotes around mid-price
- **Base Agent Interface**
  - Enforced via abstraction for extensibility

#### Engine
- **Order**
  - Represents buy/sell, market/limit orders
- **OrderBook**
  - Maintains bid and ask heaps
  - Supports best bid/ask retrieval
- **MatchingEngine**
  - Matches orders using price–time priority
  - Records executed trades
- **EventLoop**
  - Schedules and processes orders in timestamp order

#### Analytics
- **TradeTape**
  - Stores executed trades
- **SnapshotRecorder**
  - Records best bid, best ask, mid-price, and spread
- **Metrics**
  - VWAP (Volume Weighted Average Price)
  - Average spread
  - Volatility using log returns

#### Testing & Simulation
- Unit-style test for matching engine correctness
- Full simulation runner with:
  - Multiple agents
  - Random order arrivals
  - Trade execution
  - VWAP computation

---

## Key Learning Outcomes

By the end of the project, the following concepts were understood and implemented:

- Agent-based modeling of financial markets
- Order-driven market mechanics
- Matching engines and order books
- Market vs limit orders
- Liquidity provision and consumption
- Event-driven simulation
- Probabilistic understanding of risk
- Modular and extensible system design

---

