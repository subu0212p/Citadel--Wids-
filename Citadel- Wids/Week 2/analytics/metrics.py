import pandas as pd
import numpy as np

def vwap(trade_log):
    if not trade_log:
        return None

    df = pd.DataFrame(trade_log)
    traded_value = (df["price"] * df["quantity"]).sum()
    total_volume = df["quantity"].sum()
    return traded_value / total_volume


def average_spread(snapshot_data):
    valid_spreads = [
        snap["spread"] for snap in snapshot_data
        if snap.get("spread") is not None
    ]

    if not valid_spreads:
        return None

    return sum(valid_spreads) / len(valid_spreads)


def volatility(snapshot_data, lookback=10):
    mid_prices = [
        snap["mid_price"] for snap in snapshot_data
        if snap.get("mid_price") is not None
    ]

    if len(mid_prices) < lookback:
        return None

    log_returns = np.diff(np.log(mid_prices))
    return np.std(log_returns)