#############
######## data normalization with sklearn
######## based on (pseudo) randomized data
######## 50 data rows
#############
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import pandas as pd
import random

count = 50
dfRandom = pd.DataFrame({'UpTime': [random.randrange(98, 101) for _ in range(0, count)],
                        'MsgCap': [random.randrange(900, 12500) for _ in range(0, count)],
                        'NoIncidents': [random.randrange(0, 10) for _ in range(0, count)],
                        'NoLCM': [random.randrange(0, 30) for _ in range(0, count)],
                        'CyberRisk': [random.randrange(0, 50) for _ in range(0, count)],
                        'NoVulner': [random.randrange(0, 40) for _ in range(0, count)],
                        'Satisfaction': [random.randrange(5, 10) for _ in range(0, count)],
                        'SecurityRisk': [random.randrange(1, 5) for _ in range(0, count)],
                        'NoETO': [random.randrange(8, 15) for _ in range(0, count)]
                  })

print(dfRandom.describe())

scaler = MinMaxScaler()
dfNorm = scaler.fit_transform(dfRandom)
scaled_features_df = pd.DataFrame(dfNorm, columns=dfRandom.columns)

print(scaled_features_df.describe())