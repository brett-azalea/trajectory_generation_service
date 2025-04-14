#!/usr/bin/env python3
import numpy as np
import yaml
import os

def generate_control_points(n, first_cp, last_cp):
    """
    Generate n control points by linearly interpolating between first_cp and last_cp.
    Each control point is returned as a simple list of numbers.
    """
    control_points = []
    # If only one control point is requested, use the start point
    if n == 1:
        control_points.append(first_cp.tolist())
    else:
        for i in range(n):
            t = i / (n - 1)
            cp = first_cp + t * (last_cp - first_cp)
            control_points.append(cp.tolist())
    return control_points

def generate_knot_vector(n, spline_order, end_time):
    """
    Generate a clamped knot vector for a B-spline with n control points and given spline_order.
    The knot vector has total length n + spline_order.
    The first spline_order knots are 0.0, and the last spline_order knots are end_time.
    The interior knots (if any) are uniformly spaced between 0 and end_time.
    """
    total_knots = n + spline_order
    num_interior = total_knots - 2 * spline_order
    if num_interior > 0:
        # Generate 'num_interior+2' points including endpoints, then remove the endpoints
        interior = np.linspace(0, end_time, num_interior + 2)[1:-1]
        knot_points = [0.0] * spline_order + interior.tolist() + [end_time] * spline_order
    else:
        knot_points = [0.0] * spline_order + [end_time] * spline_order
    return knot_points

def main():
    # Take user input for the number of control points and the end time.
    num_points = int(input("Enter number of control points: "))
    end_time = float(input("Enter end time: "))

    # Fixed predefined values in the script:
    # These are 8-dimensional control points.
    first_cp = np.array([-1.3249999999999982, 0.0, 0.0, 0.0, 0.0, 0.0, -1.5707963267948966, 0.0])
    last_cp  = np.array([-1.6, -0.767944870877505, -0.3141592653589793, 0.3316125578789213, -0.22689280275926285,
    -0.17453292519943295, -1.0122909661567112, 0.0])
    spline_order = 5

    # Generate control points by linear interpolation and create the knot vector.
    control_points = generate_control_points(num_points, first_cp, last_cp)
    knot_points = generate_knot_vector(num_points, spline_order, end_time)

    # Package the trajectory data into a dictionary.
    waypoint_name = "waypoint_0"
    trajectory_data = {
        waypoint_name: {
            "control_points": control_points,
            "knot_points": knot_points,
            "spline_order": spline_order,
        }
    }

    # Determine the output directory relative to the location of this script.
    script_dir = os.path.dirname(os.path.realpath(__file__))
    output_dir = os.path.join(script_dir, "waypoints")
    # Create the directory if it doesn't already exist.
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Write the data to a YAML file.
    yaml_filename = os.path.join(output_dir, "trajectory_data_test.yaml")
    with open(yaml_filename, "w") as yf:
        yaml.dump(trajectory_data, yf, default_flow_style=False, indent=2)

    print(f"Trajectory data has been written to '{yaml_filename}'.")

if __name__ == "__main__":
    main()
