import datetime

def format_currency(value):
    return f"${value:,.2f}"

def format_percent(value):
    return f"{value:.2%}"

def get_current_timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def estimate_growth(capital, rate, days):
    return round(capital * ((1 + rate) ** days), 2)
