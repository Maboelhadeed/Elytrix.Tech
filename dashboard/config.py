# Configuration settings for Elytrix platform

APP_NAME = "Elytrix"
SLOGAN = "Precision Wins."
DEFAULT_CAPITAL = 100
TARGET_PROFIT_DAILY = 0.03  # 3%
BOT_MODE = "Scalping"  # Options: "Scalping", "Sniper", "Swing"

SUPPORTED_PAIRS = ["BTCUSDT", "ETHUSDT", "BNBUSDT", "SOLUSDT", "XRPUSDT"]
STRATEGY_LIST = ["AI Adaptive", "Scalping", "Sniper"]

RISK_LEVELS = {
    "Conservative": 0.01,
    "Balanced": 0.02,
    "Ultra": 0.03
}
