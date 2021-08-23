import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from constants import *


sns.set_theme()
sns.set_style("whitegrid")


# Extract Data and merge everything in one DataFrame
file_1 = OS1_WPT_PATH
file_2 = OS2_WPT_PATH
file_3 = OS1_GA_PATH
file_4 = OS2_GA_PATH

useFirstView = False
useRepeatView = not useFirstView

column_name = PLT
title_name = PLT_TITLE
isCLS = False

useGA = True
ga_column_name = GA_PLT

if useFirstView:
    title = title_name + " First View"
if useRepeatView:
    title = title_name + " Repeat View"

data_frame_1 = pd.read_csv(file_1)
data_frame_2 = pd.read_csv(file_2)
data_frame_3 = pd.read_csv(file_3)
data_frame_4 = pd.read_csv(file_4)

data_1_fv = data_frame_1[column_name].iloc[::2].reset_index(drop=True)
data_1_rv = data_frame_1[column_name].iloc[1::2].reset_index(drop=True)

data_2_fv = data_frame_2[column_name].iloc[::2].reset_index(drop=True)
data_2_rv = data_frame_2[column_name].iloc[1::2].reset_index(drop=True)

if useGA:
    data_3_ga = data_frame_3[ga_column_name]
    data_4_ga = data_frame_4[ga_column_name]

# FV or RV
if useFirstView:
    data = pd.concat([data_1_fv, data_2_fv], keys=[
        'OS1', 'OS2'], axis=1)
if useRepeatView:
    data = pd.concat([data_1_rv, data_2_rv], keys=[
        'OS1', 'OS2'], axis=1)


# Plot
# plt.style.use('grayscale')
# plt.style.use('seaborn-deep')
fig, ax1 = plt.subplots()

sns.kdeplot(
    data["OS1"],
    fill=True,
    legend=False,
    label="OS1",
)

sns.kdeplot(
    data["OS2"],
    fill=True,
    legend=False,
    label="OS2",
)

# Median
median1 = data["OS1"].median()
median2 = data["OS2"].median()
plt.axvline(median1, color='black', linestyle='solid',
            linewidth=0.5, label="Median OS1 " + str(round(median1, 3)))
plt.axvline(median2, color='black', linestyle='dashed',
            linewidth=0.5, label="Median OS2 " + str(round(median2, 3)))

# GA
if useGA:
    ga1 = data_3_ga[0] * 1000
    ga2 = data_4_ga[0] * 1000
    plt.axvline(ga1, color="tab:blue", linestyle="dashed",
                linewidth=0.8, label="GA OS1 " + str(round(ga1, 3)))
    plt.axvline(ga2, color="tab:orange", linestyle="dashed",
                linewidth=0.8, label="GA OS2 " + str(round(ga2, 3)))


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
