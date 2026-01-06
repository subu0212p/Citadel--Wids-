from abc import ABC, abstractmethod

class BaseAgent(ABC):
    def __init__(self, uid, initial_cash=100000, initial_inventory=0):
        self.uid = uid
        self.cash_balance = initial_cash
        self.position = initial_inventory

    @abstractmethod
    def decide_action(self, market_snapshot):
        """
        Decide what action to take based on the current market snapshot.
        Must be implemented by all child agent classes.
        """
        raise NotImplementedError

    def update_cash(self, amount):
        self.cash_balance += amount

    def update_position(self, quantity):
        self.position += quantity

    def __repr__(self):
        return (
            f"Agent(id={self.uid}, "
            f"cash={self.cash_balance}, "
            f"inventory={self.position})"
        )