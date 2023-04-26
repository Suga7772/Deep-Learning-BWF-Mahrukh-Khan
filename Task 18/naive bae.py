import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv("Breast_cancer_data.csv")
print(data.head(10))

# reference https://youtu.be/PPeaRc-r1OI

# print(data["diagnosis"].hist())
# plt.show()

# making heatmap to check independent variables
corr = data.iloc[:, : -1].corr(method='pearson')
cmap = sns.diverging_palette(250, 354, 80, 60, center='dark', as_cmap=True)
# print(sns.heatmap(corr, vmax=1, vmin=0.5, cmap=cmap, square=True, linewidth=0.2))
# plt.show()

# gonna compartmentalise
data = data[['mean_radius', 'mean_texture', 'mean_smoothness', 'diagnosis']]
print(data.head(10))

# fit approximate distribution

fig, axes = plt.subplots(1, 3, figsize=(18, 6), sharey=True)    # to display 3 graphs and plotting in one display
sns.histplot(data, ax=axes[0], x='mean_radius', kde=True, color='r')
sns.histplot(data, ax=axes[1], x='mean_smoothness', kde=True, color='b')
sns.histplot(data, ax=axes[2], x='mean_texture', kde=True)
# plt.show()

# calculate P(Y=y) for all possible y
def calculate_prior(df, y):
    classes = sorted(list(df[y].unique()))
    before = []
    for i in classes:
        before.append(len(df[df[y] == i]) / len(df))
    return before

# performed above logic to get the idea of how the classification algorithm workds
