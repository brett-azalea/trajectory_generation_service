#!/usr/bin/env python

import yaml
import time
from pydrake.lcm import DrakeLcm
from lcm_azalea.JointTrajectoryControllerExecutionRequest import JointTrajectoryControllerExecutionRequest
from lcm_azalea.NachiControlPoints import NachiControlPoints
from lcm_azalea.UrControlPoints import UrControlPoints
from lcm_azalea.RobotType import RobotType  # This contains the proper robot type definitions

def load_waypoints_from_yaml(filename):
    """
    Load all waypoints from the YAML file.
    Returns a list of tuples (waypoint_name, waypoint_data)
    sorted by the numerical order extracted from the waypoint name,
    e.g., "waypoint_0", "waypoint_1", etc.
    """
    with open(filename, "r") as f:
        data = yaml.safe_load(f)
    
    waypoints = []
    for key, value in data.items():
        try:
            # extract the number assuming key format "waypoint_<number>"
            num = int(key.split('_')[1])
        except (IndexError, ValueError):
            # if not a matching key, sort to the end
            num = float('inf')
        waypoints.append((num, key, value))
    
    # Sort by the numerical value
    waypoints.sort(key=lambda tup: tup[0])
    # Return a list of (key, value) tuples
    return [(k, v) for (_, k, v) in waypoints]

def publish_waypoint(waypoint_data, lcm, channel_name):
    """
    Create and publish a JointTrajectoryControllerExecutionRequest message
    based on the provided waypoint data.
    """
    # Get the trajectory details from the waypoint.
    control_points = waypoint_data.get("control_points", [])
    knot_points = waypoint_data.get("knot_points", [])
    spline_order = waypoint_data.get("spline_order", 0)
    
    # Validate control point dimensions.
    for cp in control_points:
        if len(cp) != 8:
            raise ValueError(f"Expected each control point to have 8 values but got: {cp}")
    
    control_points_size = len(control_points)
    knot_points_size = len(knot_points)
    
    # Print the loaded data for verification.
    print("Control Points:")
    for idx, cp in enumerate(control_points, 1):
        print(f"  {idx}: {cp}")
    print("\nKnot Points:")
    print(knot_points)
    print(f"\nSpline Order: {spline_order}\n")
    
    # Create and populate the JointTrajectoryControllerExecutionRequest message.
    msg = JointTrajectoryControllerExecutionRequest()
    msg.timestamp = int(time.time() * 1000)  # Current time in ms.
    msg.uuid = ""  # Optionally add a unique identifier.
    
    # Since the control points are 8-dimensional, we assume the robot type is NACHI.
    robot_type = RobotType()
    robot_type.value = RobotType.NACHI  # Use the constant defined in the RobotType message.
    msg.robot_type = robot_type
    
    msg.spline_order = spline_order
    msg.knot_points_size = knot_points_size
    
    # Populate the NachiControlPoints sub-message.
    nachi_cp = NachiControlPoints()
    nachi_cp.num_control_points = control_points_size
    nachi_cp.control_points = control_points  # Each control point must be a list of 8 floats.
    msg.nachi_control_points = nachi_cp
    
    # For UR control points, assign an empty default.
    ur_cp = UrControlPoints()
    ur_cp.num_control_points = 0
    ur_cp.control_points = []  # No UR control points provided.
    msg.ur_control_points = ur_cp
    
    # Set the knot points field.
    msg.knot_points = knot_points
    
    # Publish the message.
    encoded_message = msg.encode()
    lcm.Publish(channel_name, encoded_message)
    print(f"Published waypoint message at timestamp: {msg.timestamp}\n")

def publish_waypoints_from_yaml(yaml_filename="trajectory_data.yaml", period_seconds=0.1):
    # Load all waypoints from the YAML file.
    waypoints = load_waypoints_from_yaml(yaml_filename)
    
    if not waypoints:
        print("No waypoints found in the YAML file.")
        return
    
    # Create the LCM publisher.
    lcm = DrakeLcm()
    channel_name = "JOINT_TRAJECTORY_CONTROLLER_EXECUTION_CHANNEL"
    
    print(f"Loaded {len(waypoints)} waypoint(s) from {yaml_filename}.")
    print("Press Enter after each published waypoint to send the next one.\n")
    
    # Iterate over and publish each waypoint.
    for idx, (waypoint_name, waypoint_data) in enumerate(waypoints, start=1):
        print(f"--- Publishing {waypoint_name} ({idx}/{len(waypoints)}) ---")
        publish_waypoint(waypoint_data, lcm, channel_name)
        
        # Wait for user input before publishing the next waypoint,
        # but only if there are more waypoints remaining.
        if idx < len(waypoints):
            input("Press Enter to publish the next waypoint...")
    
if __name__ == "__main__":
    publish_waypoints_from_yaml(period_seconds=0.1)
