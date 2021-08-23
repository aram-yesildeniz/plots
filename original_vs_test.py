import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from constants import *

sns.set_theme()
sns.set_style("whitegrid")

# Extract Data and merge everything in one DataFrame
file_1 = ORIGINAL_WPT_PATH
file_2 = TEST_WPT_PATH

useFirstView = True
useRepeatView = not useFirstView

column_name = CLS
title_name = CLS_TITLE
isCLS = True


if useFirstView:
    title = title_name + " First View"
if useRepeatView:
    title = title_name + " Repeat View"

data_frame_1 = pd.read_csv(file_1)
data_frame_2 = pd.read_csv(file_2)


data_1_fv = data_frame_1[column_name].iloc[::2].reset_index(drop=True)
data_1_rv = data_frame_1[column_name].iloc[1::2].reset_index(drop=True)

data_2_fv = data_frame_2[column_name].iloc[::2].reset_index(drop=True)
data_2_rv = data_frame_2[column_name].iloc[1::2].reset_index(drop=True)

# FV or RV
if useFirstView:
    data = pd.concat([data_1_fv, data_2_fv], keys=[
        'Original', 'Test'], axis=1)
if useRepeatView:
    data = pd.concat([data_1_rv, data_2_rv], keys=[
        'Original', 'Test'], axis=1)


# Plot
# plt.style.use('grayscale')
# plt.style.use('seaborn-deep')
fig, ax1 = plt.subplots()

sns.kdeplot(
    data["Original"],
    fill=True,
    legend=False,
    label="Original",
)

sns.kdeplot(
    data["Test"],
    fill=True,
    legend=False,
    label="Test",
)

# Median
median1 = data["Original"].median()
median2 = data["Test"].median()
plt.axvline(median1, color='black', linestyle='solid',
            linewidth=0.5, label="Median Original " + str(round(median1, 3)))
plt.axvline(median2, color='black', linestyle='dashed',
            linewidth=0.5, label="Median Test " + str(round(median2, 3)))


plt.title(title)

if not isCLS:
    ax1.set_xlabel("Time (ms)")
if isCLS:
    ax1.set_xlabel("CLS Score")

plt.legend()

# sns.displot(data, kind="ecdf")
# kind="ecdf" for cumulative distribution function

plt.tight_layout()
sns.despine(left=True)
plt.gcf().savefig("__output.pdf", format='pdf')
