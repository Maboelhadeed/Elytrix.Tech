import random
import datetime

class StrategySimulator:
    def _init_(self, capital=100, strategy="Scalping", risk=0.02):
        self.capital = capital
        self.strategy = strategy
        self.risk = risk
        self.logs = []

    def simulate_day(self):
        """Simulates a trading day with profit/loss based on risk strategy."""
        profit_pct = random.uniform(-self.risk, self.risk * 1.5)
        profit = self.capital * profit_pct
        self.capital += profit

        log_entry = {
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "strategy": self.strategy,
            "daily_return": round(profit_pct * 100, 2),
            "capital": round(self.capital, 2)
        }
        self.logs.append(log_entry)
        return log_entry

    def get_logs(self):
        return self.logs

    def get_current_capital(self):
        return round(self.capital, 2)
