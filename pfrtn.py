# random PF의 기대수익률, 분산 산출함수
# 1. Ticker를 가져옵니다.
# 2. wgt를 임의로 생성하여 기대수익률을 산출합니다.
# 3. wgt에 따라 공분산 행렬을 생성하고 분산을 산출합니다.

import numpy as np
import pandas as pd
from pandas_datareader import data as web

# 1. TICKER 정보를 가져옵니다.
tickers = ['AAPL','TSLA','GOOGL','AMZN']

adjClose = pd.DataFrame()
for TICKER in tickers :
    adjClose[TICKER] = web.DataReader(TICKER, data_source = 'yahoo', start = '2019-01-01')['Adj Close']

daily_Returns = adjClose.pct_change() # Price 변화 = 수익률로 변화
Returns_mean = np.matrix(daily_Returns.mean()) # 일간수익률 평균
annual_pf_Returns = daily_Returns.mean() * 252 # 연율화

# 2. 기대수익률을 산출합니다.
number_assets = len(tickers)
wgt = np.random.random(number_assets) # random의 4개 wgt
wgt = wgt / sum( wgt )

pf_Returns = np.sum( wgt * annual_pf_Returns.T) # 연간 기대 수익률

# 3. 공분산 행렬와 리스크를 산출합니다.

wgt_pf = np.matrix(wgt)
cov = daily_Returns.cov().values
annual_cov = cov * 252
var = wgt_pf * annual_cov * wgt_pf.T

print('포트폴리오의 일별 기대수익률은', pf_Returns)
print('포트폴리오의 분산은', var)

