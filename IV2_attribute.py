import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from constants import *


sns.set_theme()
sns.set_style("whitegrid")


# Extract Data and merge everything in one DataFrame
file_1 = A1_WPT_PATH
file_2 = A2_WPT_PATH
file_3 = A3_WPT_PATH
file_4 = A1_GA_PATH
file_5 = A2_GA_PATH
file_6 = A3_GA_PATH

useFirstView = False
useRepeatView = not useFirstView

column_name = CLS
title_name = CLS_TITLE
isCLS = True

useGA = False
ga_column_name = GA_PLT

if useFirstView:
    title = title_name + " First View"
if useRepeatView:
    title = title_name + " Repeat View"

data_frame_1 = pd.read_csv(file_1)
data_frame_2 = pd.read_csv(file_2)
data_frame_3 = pd.read_csv(file_3)
data_frame_4 = pd.read_csv(file_4)
data_frame_5 = pd.read_csv(file_5)
data_frame_6 = pd.read_csv(file_6)

data_1_fv = data_frame_1[column_name].iloc[::2].reset_index(drop=True)
data_1_rv = data_frame_1[column_name].iloc[1::2].reset_index(drop=True)

data_2_fv = data_frame_2[column_name].iloc[::2].reset_index(drop=True)
data_2_rv = data_frame_2[column_name].iloc[1::2].reset_index(drop=True)

data_3_fv = data_frame_3[column_name].iloc[::2].reset_index(drop=True)
data_3_rv = data_frame_3[column_name].iloc[1::2].reset_index(drop=True)

if useGA:
    data_4_ga = data_frame_4[ga_column_name]
    data_5_ga = data_frame_5[ga_column_name]
    data_6_ga = data_frame_6[ga_column_name]

# FV or RV
if useFirstView:
    data = pd.concat([data_1_fv, data_2_fv, data_3_fv], keys=[
        'A1', 'A2', 'A3'], axis=1)
if useRepeatView:
    data = pd.concat([data_1_rv, data_2_rv, data_3_rv], keys=[
        'A1', 'A2', 'A3'], axis=1)


# Plot
# plt.style.use('grayscale')
# plt.style.use('seaborn-deep')
fig, ax1 = plt.subplots()

sns.kdeplot(
    data["A1"],
    fill=True,
    legend=False,
    label="A1",
)

sns.kdeplot(
    data["A2"],
    fill=True,
    legend=False,
    label="A2",
)

sns.kdeplot(
    data["A3"],
    fill=True,
    legend=False,
    label="A3",
)

# Median
median1 = data["A1"].median()
median2 = data["A2"].median()
median3 = data["A3"].median()
plt.axvline(median1, color='black', linestyle='solid',
            linewidth=0.5, label="Median A1 " + str(round(median1, 3)))
plt.axvline(median2, color='black', linestyle='dashed',
            linewidth=0.5, label="Median A2 " + str(round(median2, 3)))
plt.axvline(median3, color='black', linestyle='dotted',
            linewidth=0.5, label="Median A3 " + str(round(median3, 3)))

# GA
if useGA:
    ga1 = data_4_ga[0] * 1000
    ga2 = data_5_ga[0] * 1000
    ga3 = data_6_ga[0] * 1000
    plt.axvline(ga1, color="tab:blue", linestyle="dashed",
                linewidth=0.8, label="GA A1 " + str(round(ga1, 3)))
    plt.axvline(ga2, color="tab:orange", linestyle="dashed",
                linewidth=0.8, label="GA A2 " + str(round(ga2, 3)))
    plt.axvline(ga3, color="tab:green", linestyle="dashed",
                linewidth=0.8, label="GA A3 " + str(round(ga3, 3)))


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
