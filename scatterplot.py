import pandas as pd
import matplotlib.pyplot as plt

CSV_PATH = "mp2019_graph_features.csv"
df = pd.read_csv(CSV_PATH)

df = df.rename(columns={"energy_pa": "formation_energy_pa"})

plt.figure(figsize=(6, 4))
plt.scatter(df["avg_degree"], df["formation_energy_pa"], alpha=0.4)
plt.xlabel("avg_degree")
plt.ylabel("formation energy (eV/atom)")
plt.title("avg_degree vs formation energy (eV/atom)")
plt.tight_layout()
plt.show()
