# CF의 NPV와 IRR을 산출하는 함수.

import scipy as sp

cashflow = [12000, 15000, 18000, 21000, 26000]
t = 0
r = 0.015 # 1.5%
npv = -70000
for cf in cashflow :
    t = t+1
    npv = npv + cf / (1+r) ** t

print('투자안의 npv는', npv)

