import gymnasium as gym
from gymnasium import spaces
import numpy as np

class TradingEnv(gym.Env):
    """
    Minimal Trading Environment (v1)
    Discrete actions: Hold, Buy, Sell
    """

    metadata = {"render_modes": []}

    def __init__(self, max_steps=100):
        super().__init__()

        self.max_steps = max_steps

        # ----- Action Space -----
        # 0: Hold, 1: Buy, 2: Sell
        self.action_space = spaces.Discrete(3)

        # ----- Observation Space -----
        # [price, inventory, cash]
        # All normalized to [0, 1]
        self.observation_space = spaces.Box(
            low=0.0,
            high=1.0,
            shape=(3,),
            dtype=np.float32
        )

        # Internal state
        self.current_step = None
        self.price = None
        self.inventory = None
        self.cash = None

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)

        self.current_step = 0

        # Initialize market & portfolio
        self.price = 0.5          # normalized price
        self.inventory = 0.0      # normalized inventory
        self.cash = 1.0           # normalized cash

        obs = np.array(
            [self.price, self.inventory, self.cash],
            dtype=np.float32
        )

        info = {}
        return obs, info

    def step(self, action):
        assert self.action_space.contains(action), "Invalid Action"

        self.current_step += 1

        # ----- Simple price evolution -----
        price_change = np.random.normal(0, 0.01)
        self.price = np.clip(self.price + price_change, 0.0, 1.0)

        # ----- Execute Action -----
        if action == 1:  # Buy
            self.inventory += 0.1
            self.cash -= 0.1 * self.price

        elif action == 2:  # Sell
            self.inventory -= 0.1
            self.cash += 0.1 * self.price

        # ----- Portfolio Value -----
        portfolio_value = self.cash + self.inventory * self.price

        # ----- Reward (temporary: zero) -----
        reward = 0.0

        # ----- Termination Conditions -----
        terminated = False
        truncated = self.current_step >= self.max_steps

        obs = np.array(
            [self.price, self.inventory, self.cash],
            dtype=np.float32
        )

        info = {
            "portfolio_value": portfolio_value,
            "step": self.current_step
        }

        return obs, reward, terminated, truncated, info
