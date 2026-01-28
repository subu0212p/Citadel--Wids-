import gymnasium as gym
from gymnasium import spaces
import numpy as np


class TradingEnv(gym.Env):
    """
    Trading Environment with Risk-Aware Reward (Day 3 / Day 4)
    Actions:
        0 = Hold
        1 = Buy
        2 = Sell
    """

    metadata = {"render_modes": []}

    def __init__(self, max_steps=100, lambda_risk=0.01):
        super().__init__()

        self.max_steps = max_steps
        self.lambda_risk = lambda_risk

        # Action space
        self.action_space = spaces.Discrete(3)

        # Observation space (normalized)
        # [price, inventory_norm, cash_norm]
        self.observation_space = spaces.Box(
            low=0.0,
            high=1.0,
            shape=(3,),
            dtype=np.float32
        )

        # Internal state
        self.current_step = 0
        self.price = 0.5
        self.inventory = 0.0
        self.cash = 1.0

        self.prev_portfolio_value = None

    # ---------- Observation Normalization ----------
    def _get_obs(self):
        """
        Normalize observations to [0, 1]
        """
        price = self.price  # already in [0,1]

        # Inventory assumed in range [-1, 1]
        inventory_norm = (self.inventory + 1.0) / 2.0

        # Cash assumed in range [0, 2]
        cash_clipped = np.clip(self.cash, 0.0, 2.0)
        cash_norm = cash_clipped / 2.0

        return np.array(
            [price, inventory_norm, cash_norm],
            dtype=np.float32
        )

    # ---------- Reset ----------
    def reset(self, seed=None, options=None):
        super().reset(seed=seed)

        self.current_step = 0
        self.price = 0.5
        self.inventory = 0.0
        self.cash = 1.0

        self.prev_portfolio_value = self.cash + self.inventory * self.price

        obs = self._get_obs()
        info = {}

        return obs, info

    # ---------- Step ----------
    def step(self, action):
        assert self.action_space.contains(action), "Invalid action"

        self.current_step += 1

        # Price evolution
        self.price = np.clip(
            self.price + np.random.normal(0, 0.01),
            0.0,
            1.0
        )

        # Execute action
        if action == 1:  # Buy
            self.inventory += 0.1
            self.cash -= 0.1 * self.price

        elif action == 2:  # Sell
            self.inventory -= 0.1
            self.cash += 0.1 * self.price

        # Portfolio value
        current_portfolio_value = self.cash + self.inventory * self.price

        # Reward: incremental PnL - inventory risk
        pnl = current_portfolio_value - self.prev_portfolio_value
        risk_penalty = self.lambda_risk * abs(self.inventory)
        reward = pnl - risk_penalty

        self.prev_portfolio_value = current_portfolio_value

        terminated = False
        truncated = self.current_step >= self.max_steps

        obs = self._get_obs()

        info = {
            "portfolio_value": current_portfolio_value,
            "pnl": pnl,
            "inventory": self.inventory,
            "risk_penalty": risk_penalty,
            "step": self.current_step
        }

        return obs, reward, terminated, truncated, info
