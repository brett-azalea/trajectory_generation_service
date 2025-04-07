#!/usr/bin/env python

import yaml
import time
from pydrake.lcm import DrakeLcm
from lcm_azalea.JointTrajectoryControllerExecutionRequest import JointTrajectoryControllerExecutionRequest
from lcm_azalea.NachiControlPoints import NachiControlPoints
from lcm_azalea.RobotType import RobotType  # Import the proper RobotType

def load_waypoint_from_yaml(filename, waypoint="waypoint_1"):
    """
    Load a specific waypoint from a YAML file.
    """
    with open(filename, "r") as f:
        data = yaml.safe_load(f)
    if waypoint not in data:
        raise ValueError(f"Waypoint '{waypoint}' not found in {filename}")
    return data[waypoint]

def publish_joint_trajectory_from_yaml(yaml_filename="cached_trajectory_data.yaml", waypoint="waypoint_1", period_seconds=1.0):
    # Load data from the YAML file for the given waypoint.
    waypoint_data = load_waypoint_from_yaml(yaml_filename, waypoint)
    control_points = waypoint_data.get("control_points", [])
    knot_points = waypoint_data.get("knot_points", [])
    spline_order = waypoint_data.get("spline_order", 0)
    
    # Validate that each control point has 8 dimensions.
    for cp in control_points:
        if len(cp) != 8:
            raise ValueError(f"Expected each control point to have 8 values but got: {cp}")
    
    control_points_size = len(control_points)
    knot_points_size = len(knot_points)
    
    # Print the loaded data.
    print("Control Points:")
    for idx, cp in enumerate(control_points, 1):
        print(f"  {idx}: {cp}")
    
    print("\nKnot Points:")
    print(knot_points)
    
    print(f"\nSpline Order: {spline_order}\n")
    
    # Create the LCM publisher.
    lcm = DrakeLcm()
    channel_name = "JOINT_TRAJECTORY_CONTROLLER_EXECUTION_CHANNEL"
    
    print(f"Starting periodic publishing every {period_seconds} seconds on channel: {channel_name}")
    count = 0
    
    try:
        while count < 1 :
            # Create a new message for each iteration.
            msg = JointTrajectoryControllerExecutionRequest()
            msg.timestamp = int(time.time() * 1000)  # Current time in ms.
            msg.uuid = ""                         # Leave blank.
            msg.robot_type = RobotType()          # Set a proper instance.
            msg.control_points_size = control_points_size
            msg.spline_order = spline_order
            msg.knot_points_size = knot_points_size
            
            # Populate the NachiControlPoints sub-message.
            nachi_cp = NachiControlPoints()
            nachi_cp.num_control_points = control_points_size
            nachi_cp.control_points = control_points  # List of lists.
            msg.nachi_control_points = nachi_cp
            
            # Optionally, leave ur_control_points blank:
            # msg.ur_control_points = <default UrControlPoints instance>
            
            # Set the knot_points field.
            msg.knot_points = knot_points
            
            # Encode and publish the message.
            encoded_message = msg.encode()
            lcm.Publish(channel_name, encoded_message)
            
            print(f"Published JointTrajectoryControllerExecutionRequest at timestamp: {msg.timestamp}")
            time.sleep(period_seconds)
            count+=1
            
    except KeyboardInterrupt:
        print("\nStopped by user (Ctrl+C)")

if __name__ == "__main__":
    publish_joint_trajectory_from_yaml(period_seconds=0.1)
