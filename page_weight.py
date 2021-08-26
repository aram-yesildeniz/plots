import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from constants import *

sns.set_theme()
sns.set_style("whitegrid")

# Extract Data and merge everything in one DataFrame

plotRequests = False
plotBytes = not plotRequests

useFirstView = False
useRepeatView = not useFirstView

file_1 = TEST_WPT_PATH
file_2 = P1_WPT_PATH
label_file_1 = "Test"
label_file_2 = "P1"

df1 = pd.read_csv(file_1)
df2 = pd.read_csv(file_2)

request_columns = [
    REQUESTS_FULL,
    REQUESTS_HTML,
    REQUESTS_JS,
    REQUESTS_CSS,
    REQUESTS_IMAGE,
    REQUESTS_FONT,
    REQUESTS_VIDEO,
    REQUESTS_OTHER
]

request_title_columns = [
    REQUESTS_FULL_TITLE,
    REQUESTS_HTML_TITLE,
    REQUESTS_JS_TITLE,
    REQUESTS_CSS_TITLE,
    REQUESTS_IMAGE_TITLE,
    REQUESTS_FONT_TITLE,
    REQUESTS_VIDEO_TITLE,
    REQUESTS_OTHER_TITLE
]

bytes_columns = [
    BYTES_FULL,
    BYTES_HTML,
    BYTES_JS,
    BYTES_CSS,
    BYTES_IMAGE,
    BYTES_FONT,
    BYTES_VIDEO,
    BYTES_OTHER
]

bytes_title_columns = [
    BYTES_FULL_TITLE,
    BYTES_HTML_TITLE,
    BYTES_JS_TITLE,
    BYTES_CSS_TITLE,
    BYTES_IMAGE_TITLE,
    BYTES_FONT_TITLE,
    BYTES_VIDEO_TITLE,
    BYTES_OTHER_TITLE
]

if plotRequests:
    df1_filtered = df1[df1.columns.intersection(request_columns)]
    df2_filtered = df2[df2.columns.intersection(request_columns)]
if plotBytes:
    df1_filtered = df1[df1.columns.intersection(bytes_columns)]
    df2_filtered = df2[df2.columns.intersection(bytes_columns)]

df1_fv = df1_filtered.iloc[::2].reset_index(drop=True).median()
df1_rv = df1_filtered.iloc[1::2].reset_index(drop=True).median()

df2_fv = df2_filtered.iloc[::2].reset_index(drop=True).median()
df2_rv = df2_filtered.iloc[1::2].reset_index(drop=True).median()

# Plot
# plt.style.use('grayscale')
# plt.style.use('seaborn-deep')

fig, ax = plt.subplots()

n_groups = len(request_columns)
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8

if useFirstView:
    df1_fv_bars = plt.bar(index, df1_fv, bar_width,
                          alpha=opacity,
                          label=label_file_1)
    df2_fv_bars = plt.bar(index + bar_width, df2_fv, bar_width,
                          alpha=opacity,
                          label=label_file_2)

if useRepeatView:
    df1_rv_bars = plt.bar(index, df1_rv, bar_width,
                          alpha=opacity,
                          label=label_file_1)
    df2_rv_bars = plt.bar(index + bar_width, df2_rv, bar_width,
                          alpha=opacity,
                          label=label_file_2)

if plotRequests:
    title = "Requests"
    plt.xticks(index + (bar_width/2), request_title_columns)
if plotBytes:
    title = "Bytes"
    plt.xticks(index + (bar_width/2), bytes_title_columns)

if useFirstView:
    title += " First View"
if useRepeatView:
    title += " Repeat View"

plt.ylabel('Median')
plt.xlabel('Resource')
plt.title(title)
plt.legend()
plt.tight_layout()
plt.gcf().savefig("__output.pdf", format='pdf')
