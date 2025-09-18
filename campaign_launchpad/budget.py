
class GlobalBudget:
    """
    One shared marketing budget across the system.
    """
    _instance = None

    def __new__(cls, initial_amount: float = 0.0):
        # Singleton: create once, ignore subsequent initial_amount values
        if cls._instance is None:
            instance = super().__new__(cls)
            # Initialize balance only on first creation
            if initial_amount < 0:
                raise ValueError("Initial amount cannot be negative")
            instance._balance = float(initial_amount)
            cls._instance = instance
        return cls._instance

    def allocate(self, amount: float) -> None:
        # Validate allocation amount
        if amount <= 0:
            raise ValueError("Allocation amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds in the global budget")
        self._balance -= float(amount)

    def remaining(self) -> float:
        return self._balance

    def __repr__(self) -> str:
        return f"<GlobalBudget remaining={self._balance}>"
