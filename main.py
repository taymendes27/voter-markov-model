from load_data import load_data
from state_model import assign_state
from transition_matrix import build_matrix
from steady_state import steady_state

states = ["U", "R", "A", "I", "D"]

df = load_data("data/raw/ipums.csv")
df = assign_state(df)

P = build_matrix(df, states)
pi = steady_state(P)

print("Transition Matrix:\n", P)
print("Steady State:\n", pi)

