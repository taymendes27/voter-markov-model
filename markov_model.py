import numpy as np
import matplotlib.pyplot as plt

# =========================
# 1. Define states
# =========================

states = [
    "Unregistered",
    "Registered",
    "Active",
    "Inactive",
    "Disenfranchised"
]

# =========================
# 2. Transition matrix
# =========================
# Each row = current state
# Each column = next state

P = np.array([
    [0.60, 0.35, 0.00, 0.05, 0.00],  # Unregistered
    [0.10, 0.60, 0.20, 0.10, 0.00],  # Registered
    [0.05, 0.10, 0.70, 0.15, 0.00],  # Active
    [0.05, 0.10, 0.20, 0.60, 0.05],  # Inactive
    [0.00, 0.00, 0.00, 0.00, 1.00]   # Disenfranchised (absorbing)
])

# =========================
# 3. Validate matrix
# =========================

def validate_matrix(P):
    row_sums = P.sum(axis=1)
    print("Row sums (should all be 1):", row_sums)
    assert np.allclose(row_sums, 1), "Transition matrix rows must sum to 1!"

validate_matrix(P)

# =========================
# 4. Simulate Markov chain
# =========================

def simulate_chain(P, start_state=0, steps=50):
    state = start_state
    history = [state]

    for _ in range(steps):
        state = np.random.choice(len(P), p=P[state])
        history.append(state)

    return history

# =========================
# 5. Run simulation
# =========================

np.random.seed(42)  # for reproducibility

trajectory = simulate_chain(P, start_state=0, steps=50)

# Convert to readable labels
trajectory_labels = [states[i] for i in trajectory]

print("\nTrajectory:")
print(trajectory_labels)

# =========================
# 6. Plot results
# =========================

plt.figure(figsize=(10, 5))
plt.plot(trajectory, marker='o')

plt.yticks(range(len(states)), states)
plt.title("Markov Chain Simulation of Voter Registration")
plt.xlabel("Time Step")
plt.ylabel("State")

plt.grid(True)
plt.show()

# =========================
# 7. Estimate steady state (optional but impressive)
# =========================

eigvals, eigvecs = np.linalg.eig(P.T)

steady_state = eigvecs[:, np.isclose(eigvals, 1)]
steady_state = steady_state[:, 0].real
steady_state = steady_state / steady_state.sum()

print("\nSteady-state distribution:")
for s, val in zip(states, steady_state):
    print(f"{s}: {val:.4f}")
