import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

CSV_PATH = "mp2019_graph_features.csv"

df = pd.read_csv(CSV_PATH)

# Rename the target column for clarity in plots
df = df.rename(columns={"energy_pa": "formation_energy_pa"})

feature_cols = [
    "n_nodes",
    "n_edges",
    "avg_degree",
    "std_degree",
    "avg_clustering",
    "density",
]
target_col = "formation_energy_pa"

cols_for_corr = feature_cols + [target_col]
corr = df[cols_for_corr].corr()

fig, ax = plt.subplots(figsize=(8, 6))
im = ax.imshow(corr)

ax.set_xticks(range(len(cols_for_corr)))
ax.set_yticks(range(len(cols_for_corr)))
ax.set_xticklabels(cols_for_corr, rotation=45, ha="right")
ax.set_yticklabels(cols_for_corr)

cbar = fig.colorbar(im, ax=ax)
cbar.set_label("Correlation", rotation=270, labelpad=15)

for i in range(len(cols_for_corr)):
    for j in range(len(cols_for_corr)):
        value = corr.iloc[i, j]
        color = "white" if abs(value) > 0.5 else "black"
        ax.text(j, i, f"{value:.2f}", ha="center", va="center",
                color=color, fontsize=8)

plt.title("Correlation between graph features and formation energy (eV/atom)")
plt.tight_layout()
plt.show()
