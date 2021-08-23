import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from constants import *


sns.set_theme()
sns.set_style("whitegrid")


# Extract Data and merge everything in one DataFrame

file_1 = OS1_WPT_PATH
file_2 = OS2_WPT_PATH
# file_3 = A3_WPT_PATH

column_name = TTFB

data_frame_1 = pd.read_csv(file_1)
data_frame_2 = pd.read_csv(file_2)
# data_frame_3 = pd.read_csv(file_3)

data_1_fv = data_frame_1[column_name].iloc[::2].reset_index(drop=True)
data_1_rv = data_frame_1[column_name].iloc[1::2].reset_index(drop=True)

data_2_fv = data_frame_2[column_name].iloc[::2].reset_index(drop=True)
data_2_rv = data_frame_2[column_name].iloc[1::2].reset_index(drop=True)

# data_3_fv = data_frame_3[column_name].iloc[::2].reset_index(drop=True)
# data_3_rv = data_frame_3[column_name].iloc[1::2].reset_index(drop=True)


# data = pd.concat([data_1_fv, data_2_fv, data_3_fv], keys=[
#                  'P1 TTFB FV', 'P2 TTFB FV', 'P3 TTFB FV'], axis=1)

# data = pd.concat([data_1_rv, data_2_rv, data_3_rv], keys=[
#                  'P1', 'P2', 'P3'], axis=1)

data = pd.concat([data_1_fv, data_2_fv], keys=[
                 'OS1', 'OS2'], axis=1)


# Plot

g = sns.displot(
    data["OS1"],
    kind="kde",
    fill=True,
    legend=False,
    label="OS1",
)


median1 = data["OS1"].median()
median2 = data["OS2"].median()
plt.axvline(median1, color='black', linestyle='solid',
            linewidth=0.5, label="Median P1")
plt.axvline(median2, color='black', linestyle='dashed',
            linewidth=0.5, label="Median P1")

g.set_axis_labels("Time (ms)")
g.set(title='TTFB First View')

# plt.legend(loc='upper right')
handles, labels = plt.gca().get_legend_handles_labels()
print(handles)
print(labels)
# plt.legend(loc='upper right', labels=[
#            'Median 1', 'Median 2', "OS2", "OS1"])


# sns.displot(data, kind="ecdf")
# kind="ecdf" for cumulative distribution function


# plt.show()
plt.tight_layout()
sns.despine(left=True)
plt.gcf().savefig("__output.pdf", format='pdf')
