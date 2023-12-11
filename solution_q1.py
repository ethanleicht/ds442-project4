import numpy as np
import pandas as pd
from math import fsum

# Define the BN
P_B = pd.DataFrame({'B': [1,0],
                    'P': [.001,.999]})

P_E = pd.DataFrame({'E': [1,0],
                    'P': [.002,.998]})

P_J_given_A = pd.DataFrame({'A': [1,1,0,0],
                            'J': [1,0,1,0],
                            'P': [.9,.1,.05,.95]})

P_M_given_A = pd.DataFrame({'A': [1,1,0,0],
                            'M': [1,0,1,0],
                            'P': [.7,.3,.01,.99]})

P_A_given_BE = pd.DataFrame({'B': [1,1,1,1,0,0,0,0],
                             'E': [1,1,0,0,1,1,0,0],
                             'A': [1,0,1,0,1,0,1,0],
                             'P': [.95,.05,.94,.06,.29,.71,.001,.999]})

# Create f1(A)
f1 = pd.DataFrame({'A': [1,0]})
f1['P'] = [sum(P_M_given_A.query(f'A=={a}')['P']) for a in [1,0]]
print(f1)

# Create f2(B,E,+j)
f2 = pd.DataFrame({'B': [1,1,0,0],
                   'E': [1,0,1,0]})
f2_P = []
for b,e in [1,1],[1,0],[0,1],[0,0]:
    sum = 0
    for a in [1,0]:
        sum += P_A_given_BE.query(f'A=={a} & B=={b} & E=={e}')['P'].item() * P_J_given_A.query(f'A=={a} & J==1')['P'].item() * f1.query(f'A=={a}')['P'].item()
    f2_P.append(sum)
f2['P'] = f2_P
print(f2)

# Create final factor, f3(B,+j)
f3 = pd.DataFrame({'B': [1,0]})
f3_P = []
for b in [1,0]:
    sum = 0
    for e in [1,0]:
        sum += P_E.query(f'E=={e}')['P'].item() * f2.query(f'B=={b} & E=={e}')['P'].item()
    f3_P.append(sum)
f3['P'] = f3_P
print(f3)

# Normalize
result = pd.DataFrame({'B': [1,0]})
Z = fsum(f3_P)
result['P(B|+j)'] = [f3.query(f'B=={b}')['P'].item()/Z for b in [1,0]]

# Print final result
print(result)