# Citadel × WiDS – Agent-Based Market Simulation Project

This repository documents a three-week learning and implementation project focused on
financial markets, market microstructure, agent-based modeling, and reinforcement learning.
The project progresses from foundational quantitative concepts to a complete
multi-agent market simulator with behavioral analysis and benchmarking.

---

## Week 0: Foundations – Python, Randomness, and Risk

### Work Done
- Revised Python fundamentals relevant for quantitative finance
- Implemented **Geometric Brownian Motion (GBM)** for asset price simulation
- Simulated multiple GBM price paths with identical parameters
- Visualized:
  - Price trajectories
  - Distribution of final prices
- Wrote a reflection on randomness and financial risk

### Key Concepts Learned
- Financial markets are inherently stochastic
- Identical model parameters can lead to widely different outcomes
- Risk is a distribution, not a point estimate
- Volatility controls uncertainty and dispersion
- Losses are natural outcomes, not anomalies

---

## Week 1: Market Microstructure & System Design

### Work Done
- Studied internal mechanics of electronic exchanges
- Designed a modular **limit order book (LOB) based market architecture**
- Defined clear interfaces between:
  - Agents
  - Market environment
  - Order book
  - Matching engine
  - Analytics layer

### Architecture Overview
- **Agents**
  - Observe partial market state
  - Decide actions
  - Submit orders
- **Market Environment**
  - Maintains simulation clock
  - Routes agent orders
- **Order Book**
  - Maintains bid and ask sides
  - Enforces price–time (FIFO) priority
- **Matching Engine**
  - Executes trades and handles partial fills
- **Analytics**
  - Trade tape, spreads, depth, and mid-price tracking

### Key Concepts Learned
- Order-driven market mechanics
- Liquidity provision vs liquidity consumption
- Bid–ask spread formation
- Event-driven simulation
- Importance of modular system design

---

## Week 2: Agent-Based Exchange & Emergent Market Dynamics

### Work Done
- Implemented a complete agent-based market simulator
- Added heterogeneous agents interacting through a shared order book

### Agents Implemented
- **Noise Traders**
  - Random buy/sell actions
  - Primary source of stochastic order flow
- **Momentum Traders**
  - Trend-following agents using moving averages
  - Create feedback loops and instability
- **Market Makers**
  - Two-sided limit quoting
  - Spread capture with inventory control

### Experiments & Analysis
- Order book heatmaps to visualize liquidity concentration
- Spread and mid-price evolution
- Volatility clustering analysis
- Return distribution analysis showing fat tails
- Scenario-based simulations:
  - Noise-only market
  - Noise + market makers
  - Noise + momentum traders

### Key Observations
- Market makers stabilize spreads and prices
- Momentum traders amplify volatility and crashes
- Stylized facts emerge without being hard-coded

---

## Week 3: Reinforcement Learning, Behavioral Analysis & Benchmarking

### Work Done
- Integrated a **Reinforcement Learning (RL) trader** using PPO
- Built a custom **Gymnasium-compatible trading environment**
- Designed a **risk-aware reward function** incorporating PnL and penalties
- Trained and validated learning behavior
- Performed systematic analysis of agent behavior and market outcomes

### Reinforcement Learning Setup
- **State:** Market features (mid-price, spread) + agent inventory
- **Actions:** Buy, Sell, Hold (discrete)
- **Reward:** Incremental portfolio value with risk penalties
- **Algorithm:** PPO (Stable-Baselines3)

### Behavioral & Statistical Analysis
- **Herding Detection**
  - Correlation analysis of agent positions
  - Identification of synchronization during stress
- **Stylized Facts Validation**
  - Volatility clustering
  - Fat-tailed return distributions

### Benchmarking & Evaluation
- Compared RL agent performance against:
  - Buy & Hold strategy
  - Random trading agent
- Metrics used:
  - Sharpe Ratio
  - Maximum Drawdown
  - Equity curves and drawdown plots

### Visualization
- Interactive dashboards using Plotly
- Order book heatmaps
- Equity curve and PnL distribution plots

### Key Insights
- Learning is highly sensitive to reward design
- Apparent profitability without benchmarks is misleading
- Herding emerges as a collective phenomenon, not individual behavior
- Risk-adjusted metrics are essential for evaluating trading strategies

---

## Final Outcome

By the end of the project, the following were achieved:

- A fully functional agent-based market simulator
- Reinforcement learning integrated with market microstructure
- Endogenous emergence of volatility, crashes, and herding
- Behavioral validation and benchmarking against baseline strategies
- A complete experimental and reporting pipeline

This project demonstrates how complex market behavior can emerge from
simple rules, constraints, and agent interactions—without being explicitly programmed.

---
