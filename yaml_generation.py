#!/usr/bin/env python3
import numpy as np
import yaml

# Define the new control points as a list of NumPy arrays.
control_points = [
    np.array([[-1.32500000e+00],
              [ 0.00000000e+00],
              [-3.31105683e-18],
              [-9.76578736e-18],
              [-5.44623060e-18],
              [ 8.83848702e-19],
              [-1.57079633e+00],
              [-1.48029737e-16]]),
    np.array([[-1.32500000e+00],
              [ 0.00000000e+00],
              [-3.31105683e-18],
              [-9.76578736e-18],
              [-1.93240184e-17],
              [ 8.83848702e-19],
              [-1.57079633e+00],
              [-1.48029737e-16]]),
    np.array([[-1.32485926e+00],
              [ 1.60057313e-04],
              [ 6.85653476e-05],
              [ 2.87426271e-04],
              [ 5.84187376e-04],
              [-1.58095245e-03],
              [-1.57060102e+00],
              [ 7.93331478e-02]]),
    np.array([[-1.32519765e+00],
              [-2.76372613e-04],
              [ 2.33968996e-04],
              [ 7.12901268e-04],
              [ 1.32456904e-04],
              [-3.00528776e-03],
              [-1.57097956e+00],
              [ 1.98332870e-01]]),
    np.array([[-1.32516738e+00],
              [ 2.83729009e-04],
              [ 6.94678802e-04],
              [ 3.95961499e-04],
              [ 5.46799879e-04],
              [-4.05140740e-03],
              [-1.57092415e+00],
              [ 3.56999165e-01]]),
    np.array([[-1.32528154e+00],
              [ 2.04477037e-04],
              [ 2.36755996e-04],
              [ 7.57258328e-04],
              [-1.02170844e-04],
              [-3.54679294e-03],
              [-1.57054705e+00],
              [ 5.15665461e-01]]),
    np.array([[-1.32495663e+00],
              [ 2.11212566e-04],
              [-3.33567005e-04],
              [ 4.09261058e-04],
              [ 1.08309305e-04],
              [-2.02243557e-03],
              [-1.57072017e+00],
              [ 6.74331756e-01]]),
    np.array([[-1.32509551e+00],
              [-4.65299712e-05],
              [-6.46591860e-04],
              [ 3.84915138e-04],
              [-2.47236094e-04],
              [-6.42502666e-04],
              [-1.57097078e+00],
              [ 7.93331478e-01]]),
    np.array([[-1.32500000e+00],
              [ 7.12470910e-20],
              [-1.01748085e-18],
              [ 1.09037063e-17],
              [ 4.87773939e-17],
              [-3.81478066e-17],
              [-1.57079633e+00],
              [ 8.72664626e-01]]),
    np.array([[-1.32500000e+00],
              [ 7.12470910e-20],
              [-1.01748085e-18],
              [ 1.09037063e-17],
              [ 4.87773939e-17],
              [-3.81478066e-17],
              [-1.57079633e+00],
              [ 8.72664626e-01]])
]

# Convert each NumPy array into a flattened list (to remove extra nesting).
flattened_control_points = [
    [elem for sublist in cp.tolist() for elem in sublist]
    for cp in control_points
]

# Define the new knot points.
knot_points = [
    0.0, 0.0, 0.0, 0.0, 0.0,
    3.9666573908961915, 7.933314781792383, 11.899972172688575,
    15.866629563584766, 19.833286954480958, 23.79994434537715,
    23.79994434537715, 23.79994434537715, 23.79994434537715,
    23.79994434537715
]

spline_order = 5

# Create the trajectory data dictionary with a specific waypoint name.
trajectory_data = {}
waypoint_name = "waypoint_1"

trajectory_data[waypoint_name] = {
    "control_points": flattened_control_points,
    "knot_points": knot_points,
    "spline_order": spline_order,
}

# Dump the data into a YAML file with proper formatting.
yaml_filename = "cached_trajectory_data_2.yaml"
with open(yaml_filename, "a") as yaml_file:
    yaml.dump(trajectory_data, yaml_file, default_flow_style=None, indent=2)

print(f"Trajectory data has been appended to '{yaml_filename}'.")
