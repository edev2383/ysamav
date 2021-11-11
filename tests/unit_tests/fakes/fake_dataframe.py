import pandas as pd
from .. import IScraperPayload


def fake_history():
    close = [8, 9, 10, 11, 12, 13]
    open = [7, 8, 9, 10, 11, 12]
    high = [9, 10, 11, 12, 13, 14]
    low = [6, 7, 8, 9, 10, 11]
    adjclose = [8, 9, 10, 11, 12, 13]
    volume = [10000, 11000, 12000, 10000, 9000, 14000]
    d = {
        "High": high,
        "Low": low,
        "Open": open,
        "Close": close,
        "Adj_Close": adjclose,
        "Volume": volume,
    }
    payload = IScraperPayload()
    payload.dataframe = pd.DataFrame(data=d)
    return payload


def fake_current():
    df = fake_history()
    payload = IScraperPayload()
    payload.date = "2021-11-07"
    payload.high = df.iloc[0]["High"]
    payload.low = df.iloc[0]["Low"]
    payload.open = df.iloc[0]["Open"]
    payload.close = df.iloc[0]["Close"]
    payload.adjclose = df.iloc[0]["Adj_Close"]
    payload.volume = df.iloc[0]["Volume"]
    return payload
