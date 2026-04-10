import pandas as pd
import numpy as np

# 1. Load data
df = pd.read_csv("data/cps_voting_2024.csv")

print(df.head())

# 2. Clean relevant columns
# Example placeholders:
registered = df["registered"]
voted = df["voted"]

# 3. Estimate probabilities

P_registered_to_active = np.sum((registered == 1) & (voted == 1)) / np.sum(registered == 1)

P_registered_to_inactive = 1 - P_registered_to_active

print("P(R → A):", P_registered_to_active)
print("P(R → I):", P_registered_to_inactive)

# 4. transition matrix 
P = np.array([
    [0.7, 0.3],
    [0.2, 0.8]
])
