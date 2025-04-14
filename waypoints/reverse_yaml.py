#!/usr/bin/env python3
import yaml
import argparse

def reverse_control_points(input_file, output_file):
    # Open and load the YAML file.
    with open(input_file, "r") as f:
        data = yaml.safe_load(f)
    
    # Iterate over each waypoint and reverse the order of its control points.
    for waypoint_name, trajectory in data.items():
        if 'control_points' in trajectory:
            original_cps = trajectory['control_points']
            trajectory['control_points'] = list(reversed(original_cps))
            print(f"Reversed control points for {waypoint_name}.")
        else:
            print(f"No control points found for {waypoint_name}; skipping.")

    # Write the updated data in block style format.
    with open(output_file, "w") as f:
        yaml.dump(data, f, default_flow_style=False, indent=2)
    print(f"Reversed trajectory data has been written to '{output_file}'.")

def main():
    parser = argparse.ArgumentParser(
        description="Reverse the order of control points in a YAML trajectory file."
    )
    parser.add_argument("input", help="Path to the input YAML file containing trajectory data.")
    parser.add_argument("output", help="Path to the output YAML file with reversed control points.")
    args = parser.parse_args()
    
    reverse_control_points(args.input, args.output)

if __name__ == "__main__":
    main()
