# Day 1 – Trading as a Markov Decision Process (MDP)

## Overview

In this project, algorithmic trading is formulated as a Markov Decision Process (MDP) to enable reinforcement learning.  
An MDP provides a structured framework for sequential decision-making under uncertainty, which naturally aligns with financial markets.

An MDP is defined by the tuple

(S, A, P, R, γ)

Each component is mapped explicitly to the trading system.

---

## 1. Agent–Environment Interaction

At each timestep t

- The agent observes the current state S_t
- The agent takes an action A_t
- The environment returns a reward R_t
- The system transitions to the next state S_{t+1}

### Trading Interpretation

- Agent Trading strategy (RL policy)
- Environment Market microstructure + execution logic
- Interaction loop
  - Observe market and portfolio state
  - Execute trade or remain idle
  - Receive profitloss adjusted for costs
  - Transition to the next market state

Each action influences future opportunities, making the problem inherently sequential.

---

## 2. State Space (S)

The state contains all information required to make an optimal decision under the Markov assumption.

### Market Features
- Top-k bid prices
- Top-k ask prices
- Corresponding bidask volumes
- Mid-price and bid–ask spread

### Portfolio Features
- Current inventory
- Cash balance
- Unrealized PnL

### Design Rationale
- The state must be rich enough to capture short-term market dynamics
- Excessive dimensionality is avoided to reduce learning complexity

The state is represented as a fixed-length numerical vector and normalized for numerical stability.

---

## 3. Action Space (A)

A discrete action space is used for initial prototyping.

 Action  Description 
------------------
 0  Hold 
 1  Buy one unit 
 2  Sell one unit 

### Motivation
- Easier debugging
- Stable learning behavior
- Clear reward attribution

---

## 4. Reward Function (R)

The reward encodes the optimization objective of the agent.

Baseline reward formulation

R_t = V_t − V_{t−1} − transaction costs

Where
- V_t is the portfolio value at time t

Optional penalties (introduced later)
- Inventory risk
- Drawdown
- Volatility

The agent optimizes exactly what is specified in the reward function.

---

## 5. Transition Dynamics (P)

Market dynamics are unknown and non-stationary.

- The agent does not have access to an explicit transition model
- Learning occurs through observed state transitions
- The environment simulates market behavior deterministically or stochastically

---

## 6. Discount Factor (γ)

The discount factor controls time preference.

- γ close to 1 encourages long-term planning and inventory awareness
- γ closer to 0 favors short-term profit extraction

In this project, γ reflects the economic horizon of the trading strategy.

---

## Conclusion

By framing trading as an MDP, the problem becomes suitable for reinforcement learning.  
Clear definitions of state, action, reward, and episode structure are essential before implementing the environment or training agents.

This MDP formulation serves as the foundation for all subsequent stages of the project.
