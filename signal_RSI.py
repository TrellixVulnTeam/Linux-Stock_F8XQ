# coding:utf8
import pandas as pd
from lib.rsi import rsi
from settings import engine_ts
ts_code = "002480.SZ"
sql = "select trade_date,close from `daily_{}` order by trade_date DESC limit 100;".format(ts_code)
df = pd.read_sql_query(sql=sql, con=engine_ts, index_col=None, coerce_float=True, params=None, parse_dates=None, chunksize=None)
close = df.close
# df["RSI"] = rsi(close=close, length=6, drift=0, offset=0)
# print df
print rsi(close=close, length=6, drift=0, offset=0)
import matplotlib.pyplot as plt
df.plot(x='trade_date', kind='line', figsize=(20, 8), grid=True)
plt.show()
