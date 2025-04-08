#!/usr/bin/env python3
import argparse
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():
    parser = argparse.ArgumentParser(
        description="Plot measured vs desired joint values over time from a CSV log."
    )
    parser.add_argument(
        "csv_file", help="Path to the CSV file containing the logged data."
    )
    parser.add_argument(
        "--joint", type=int, default=4,
        help="The joint number to plot (0-7). Default is 4."
    )
    args = parser.parse_args()

    # Load the CSV file. We assume the file has no header.
    df = pd.read_csv(args.csv_file, header=None)

    # Normalize time by subtracting the first timestamp.
    time = df[0] - df[0].iloc[0]

    # Extract measured and desired values.
    # Column 0: time, Columns 1-8: measured joints, Columns 9-16: desired joints.
    measured = df[args.joint + 1]         # +1 because column 0 is time.
    desired = df[args.joint + 1 + 8]        # +1 for time column and +8 to skip measured joints.

    # measured = df[args.joint]         # args.joint maps directly to measured joint columns (1-8).
    # desired = df[args.joint+8] 

    # Create the plot.
    plt.figure(figsize=(10, 6))
    plt.plot(time, measured, label=f"Measured Joint {args.joint}", marker="o")
    # plt.plot(time, desired, label=f"Desired Joint {args.joint}", linestyle="--")
    plt.plot(time, desired, label=f"Desired Joint {args.joint}", marker="o")
    plt.xlabel("Normalized Time (s)")
    plt.ylabel("Joint Value")
    plt.title(f"Measured vs Desired Values for Joint {args.joint}")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
