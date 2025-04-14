#!/usr/bin/env python

from pydrake.lcm import DrakeLcm
from lcm_azalea.JointTrajectoryControllerExecutionRequest import JointTrajectoryControllerExecutionRequest
from lcm_azalea.NachiJointAngles import NachiJointAngles
import numpy as np
import time

def read_control_points(filename):
    """
    Reads the control points from a CSV file.
    The CSV is expected to have either:
      - 50 rows x 8 columns, or
      - 8 rows x 50 columns (in which case the data is transposed).
    """
    data = np.loadtxt(filename, delimiter=',')
    if data.shape == (8, 50):
        data = data.transpose()
    return data

def read_knot_points(filename):
    """
    Reads the knot vector from a CSV file.
    The CSV is expected to have 1 row (or column) of 55 numbers.
    """
    data = np.loadtxt(filename, delimiter=',')
    return data.flatten()

def publish_joint_trajectory_controller(period_seconds=1.0):
    lcm = DrakeLcm()
    channel_name = "JOINT_TRAJECTORY_CONTROLLER_EXECUTION_CHANNEL"
    
    # Read data from CSV files (this is done once before entering the publish loop).
    control_points = read_control_points("control_points.csv")
    knot_points = read_knot_points("knot_vector.csv")
    
    # Validate data dimensions.
    if control_points.shape != (50, 8):
        print(f"Error: Expected control_points shape (50, 8), but got {control_points.shape}")
        return
    if knot_points.shape[0] != 55:
        print(f"Error: Expected knot_vector length 55, but got {knot_points.shape[0]}")
        return
    
    print(f"Starting periodic publishing every {period_seconds} seconds on channel: {channel_name}")
    
    try:
        while True:
            # Create a new message for each iteration.
            msg = JointTrajectoryControllerExecutionRequest()
            msg.timestamp = int(time.time() * 1000)  # Current time in milliseconds
            msg.control_points_size = 50
            msg.spline_order = 5
            msg.knot_points_size = 55
            
            # Populate the control_points array.
            msg.control_points = []
            for cp in control_points:
                joint_angles = NachiJointAngles()
                joint_angles.q = cp.tolist()  # Convert numpy array to list of 8 floats.
                msg.control_points.append(joint_angles)
            
            # Populate the knot_points array.
            msg.knot_points = knot_points.tolist()
            
            # Encode and publish the message.
            encoded_message = msg.encode()
            lcm.Publish(channel_name, encoded_message)
            
            print(f"Published joint_trajectory_controller message at timestamp: {msg.timestamp}")
            # for idx, cp in enumerate(msg.control_points):
            #     print(f"Control Point {idx+1}: " + " ".join(map(str, cp.q)))
            
            time.sleep(period_seconds)
            
    except KeyboardInterrupt:
        print("\nStopped by user (Ctrl+C)")

if __name__ == "__main__":
    publish_joint_trajectory_controller(period_seconds=1.0)
