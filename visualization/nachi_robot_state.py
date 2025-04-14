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
    measured_deg = measured * (180. / np.pi)
    desired_deg = desired * (180. / np.pi)

    # Create the plot.
    # plt.figure(figsize=(10, 6))
    # plt.plot(time, measured*(180./np.pi), label=f"Measured Joint {args.joint}", marker="o")
    # # plt.plot(time, desired, label=f"Desired Joint {args.joint}", linestyle="--")
    # plt.plot(time, desired*(180./np.pi), label=f"Desired Joint {args.joint}", marker="o")
    # plt.xlabel("Normalized Time (s)")
    # plt.ylabel("Joint Value")
    # plt.title(f"Measured vs Desired Values for Joint {args.joint}")
    # plt.legend()
    # plt.grid(True)
    # plt.tight_layout()
    # plt.show()

    # Create the plot.
    plt.figure(figsize=(10, 6))
    plt.plot(time, measured_deg, label=f"Measured Joint {args.joint}", marker="o")
    plt.plot(time, desired_deg, label=f"Desired Joint {args.joint}", marker="o")

    # Increase font sizes for the axes labels and title.
    plt.xlabel("Time (s)", fontsize=25)
    plt.ylabel("Joint Value (deg)", fontsize=25)
    plt.title(f"Measured vs Desired Values for Joint {args.joint}", fontsize=30)
    plt.legend(fontsize=25)

    # Limit the x-axis from 0 to 1 second.
    plt.xlim(0, 0.8)
    plt.ylim(-90, -86.5)
    plt.xticks(fontsize=25)
    plt.yticks(fontsize=25)

    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
