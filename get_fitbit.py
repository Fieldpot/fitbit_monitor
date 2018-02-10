import fitbit
import pandas as pd
import numpy as np
from config import *

authd_client = fitbit.Fitbit(CLIENT_ID, CLIENT_SECRET
                             ,access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN)

DATE = "2018-02-01"

data_sec = authd_client.intraday_time_series('activities/heart', DATE, detail_level='15min') #'1sec', '1min', or '15min'
heart_sec = data_sec["activities-heart-intraday"]["dataset"]
heart_sec[:10]
print(heart_sec)
