import pandas as pd
import matplotlib.pyplot as plt
import os
import argparse

argparser = argparse.ArgumentParser(description='Visualize Nachi State Variables')
argparser.add_argument('--path', type=str, help='Path to the CSV file')
argparser.add_argument('--joint', type=int, default=None, help='Joint number to visualize (0-7). If not specified, all joints will be shown.')

args = argparser.parse_args()
if args.path is None:
    raise ValueError("Please specify a path with the --path argument")

absolute_path = os.path.abspath(args.path)

# Check if the file exists
if not os.path.exists(absolute_path):
    raise FileNotFoundError(f"File not found at: {absolute_path}")

# Define column names based on the CSV structure
column_names = ['time'] + [f'measured_q{i}' for i in range(8)] + [f'desired_q{i}' for i in range(8)]

# Read CSV file
df = pd.read_csv(absolute_path, header=None, names=column_names)

# Normalize time to start at 0
first_time = df['time'].iloc[0] if not df.empty else 0
df['time'] = df['time'] - first_time

if args.joint is not None:
    if args.joint < 0 or args.joint > 7:
        raise ValueError("Joint number must be between 0 and 7")
    
    # Create a single plot for the specified joint
    plt.figure(figsize=(10, 6))
    plt.plot(df['time'], df[f'measured_q{args.joint}'], 'bo-', linewidth=1.5, markersize=4, label='Measured')
    plt.plot(df['time'], df[f'desired_q{args.joint}'], 'ro-', linewidth=1.5, markersize=4, label='Desired')
    plt.xlabel('Time (s)')
    plt.ylabel(f'Joint {args.joint} Angle')
    plt.title(f'Joint {args.joint} Measured vs Desired Angle')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
else:
    # Create subplots for all joints
    plt.figure(figsize=(12, 16))
    
    for i in range(8):
        plt.subplot(8, 1, i+1)
        plt.plot(df['time'], df[f'measured_q{i}'], 'bo-', linewidth=1.0, markersize=3, label='Measured')
        plt.plot(df['time'], df[f'desired_q{i}'], 'ro-', linewidth=1.0, markersize=3, label='Desired')
        plt.ylabel(f'Joint {i}', fontsize=10)
        plt.grid(True, linestyle='--', alpha=0.7)
        
        if i == 0:
            plt.legend(loc='upper right')
        
        if i < 7:
            plt.tick_params(labelbottom=False)
        else:
            plt.xlabel('Time (s)')
    
    plt.suptitle('Joint Angles: Measured vs Desired', y=0.92)

plt.tight_layout()
plt.show()
