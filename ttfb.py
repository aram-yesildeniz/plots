import seaborn as sns
import pandas as pd
from constants import *


sns.set_theme()

file_1 = ORIGINAL_PATH
column_name = "TTFB"

data_frame_1 = pd.read_csv(file_1)

data_1_fv = data_frame_1[column_name].iloc[::2]
data_1_rv = data_frame_1[column_name].iloc[1::2]

print(data_1_rv)
