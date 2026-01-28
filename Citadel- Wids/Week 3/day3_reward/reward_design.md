# Day 3 – Reward Function Engineering

## Objective

The reward function defines the agent’s optimization objective.
In this project, the reward is designed to balance **profitability** and **risk control**.

---

## Reward Formulation

The reward at timestep t is defined as:

Reward_t = (V_t - V_{t-1}) - λ · |Inventory_t|

Where:
- V_t is the current portfolio value
- V_{t-1} is the previous portfolio value
- λ is the risk aversion coefficient

---

## Incremental PnL

Using incremental portfolio value change provides:
- Dense rewards
- Clear credit assignment
- Faster learning

This avoids the instability associated with sparse, end-of-episode rewards.

---

## Risk Penalty

An inventory-based penalty is applied to discourage:
- Large directional exposure
- Inventory hoarding
- Excessive risk-taking

This ensures the agent learns **risk-adjusted decision making**, not raw profit maximization.

---

## Design Considerations

- Reward is deterministic
- Reward is numerically stable
- Diagnostics (PnL, inventory, risk) are logged separately
- Reward is not clipped or normalized

This reward function is well-posed and suitable for policy optimization.
