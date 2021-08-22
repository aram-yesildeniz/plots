import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from constants import *


sns.set_theme()

# Extract Data and merge everything in one DataFrame

file_1 = ORIGINAL_PATH
column_name = "TTFB"

data_frame_1 = pd.read_csv(file_1)

data_1_fv = data_frame_1[column_name].iloc[::2].reset_index(drop=True)
data_1_rv = data_frame_1[column_name].iloc[1::2].reset_index(drop=True)

data = pd.concat([data_1_fv, data_1_rv], keys=['TTFB_FV', 'TTFB_RV'], axis=1)
print(data)


# Plot

sns.displot(data, kde=True)
plt.show()


# kind="ecdf" for cumulative distribution function
