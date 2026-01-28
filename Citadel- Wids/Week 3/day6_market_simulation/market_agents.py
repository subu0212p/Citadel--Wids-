import numpy as np


# ======================================================
# Noise Trader
# ======================================================
class NoiseTrader:
    def __init__(self, agent_id, max_inventory=10):
        self.agent_id = agent_id
        self.inventory = 0
        self.max_inventory = max_inventory

    def can_buy(self):
        return self.inventory < self.max_inventory

    def can_sell(self):
        return self.inventory > -self.max_inventory

    def act(self, market):
        action = np.random.choice(["buy", "sell"])

        if action == "buy" and not self.can_buy():
            return None
        if action == "sell" and not self.can_sell():
            return None

        if action == "buy":
            self.inventory += 1
        else:
            self.inventory -= 1

        return {
            "agent_id": self.agent_id,
            "side": action,
            "price": market.mid_price,
            "volume": 1,
            "type": "market"
        }


# ======================================================
# Market Maker
# ======================================================
class MarketMaker:
    def __init__(self, agent_id, spread=0.02, quote_volume=10):
        self.agent_id = agent_id
        self.spread = spread
        self.quote_volume = quote_volume
        self.inventory = 0

    def act(self, market):
        mid = market.mid_price

        bid_price = mid - self.spread / 2
        ask_price = mid + self.spread / 2

        return [
            {
                "agent_id": self.agent_id,
                "side": "buy",
                "price": bid_price,
                "volume": self.quote_volume,
                "type": "limit"
            },
            {
                "agent_id": self.agent_id,
                "side": "sell",
                "price": ask_price,
                "volume": self.quote_volume,
                "type": "limit"
            }
        ]


# ======================================================
# RL Trader (Frozen Policy Placeholder)
# ======================================================
class RLTrader:
    def __init__(self, agent_id, policy=None, max_inventory=20):
        self.agent_id = agent_id
        self.inventory = 0
        self.policy = policy
        self.max_inventory = max_inventory

    def act(self, market):
        # Placeholder behavior (safe + bounded)
        action = np.random.choice(["buy", "sell"])

        if action == "buy" and self.inventory >= self.max_inventory:
            return None
        if action == "sell" and self.inventory <= -self.max_inventory:
            return None

        if action == "buy":
            self.inventory += 1
        else:
            self.inventory -= 1

        return {
            "agent_id": self.agent_id,
            "side": action,
            "price": market.mid_price,
            "volume": 1,
            "type": "market"
        }
