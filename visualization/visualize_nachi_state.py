import pandas as pd
import matplotlib.pyplot as plt
import os

relative_path = "../logs/nachi_mr50/investor_demo_state_data.csv"
absolute_path = os.path.abspath(relative_path)

# Check if the file exists
if not os.path.exists(absolute_path):
    raise FileNotFoundError(f"File not found at: {absolute_path}")

# Read CSV file (assumes no header)
df = pd.read_csv(absolute_path, header=None, names=['time', 'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6'])

# Create figure with subplots
plt.figure(figsize=(10, 8))

# Normalize time to start at 0
df['time'] = df['time'] - df['time'][0]

# Plot each state variable
for i in range(0,7):
    plt.subplot(7, 1, i+1)
    plt.plot(df['time'], df[f'q{i}'], 'bo-', linewidth=1.5)
    plt.ylabel(f'q{i}', fontsize=10)
    if i < 6:
        plt.tick_params(labelbottom=False)  # hide x-axis labels for all but bottom plot
    else:
        plt.xlabel('Time (s)')

plt.suptitle('State Variables vs Time', y=0.92)
plt.tight_layout()
plt.show()
