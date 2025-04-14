#!/usr/bin/env python
import time
from pydrake.lcm import DrakeLcm
from lcm_azalea.CartesianVelocityControllerExecutionRequest import CartesianVelocityControllerExecutionRequest
from lcm_azalea.RobotType import RobotType
from lcm_azalea.Twist6d import Twist6d

def publish_cartesian_velocity_request():
    # Create an LCM publisher.
    lcm = DrakeLcm()
    channel = "CARTESIAN_VELOCITY_CONTROLLER_EXECUTION_CHANNEL"

    # Create and populate the CartesianVelocityControllerExecutionRequest message.
    msg = CartesianVelocityControllerExecutionRequest()
    msg.timestamp = int(time.time() * 1000)    # Current time in milliseconds.
    msg.uuid = "unique-request-id"              # A unique identifier for the request.

    # Set the robot type (using UR, which is 0 according to messages.lcm).
    robot_type = RobotType()
    robot_type.value = RobotType.NACHI  # Set the robot type to UR.
    msg.robot_type = robot_type

    # Populate the Twist6d for the end-effector velocity.
    twist = Twist6d()
    twist.v_xyz = [0.0, 0.0, -1.]               # Linear velocity vector (m/s).
    twist.w_xyz = [0.0, 0.0, 0.0]               # Angular velocity vector (rad/s).
    msg.v_end_effector = twist

    # Set end condition flags and parameters.
    msg.should_exit_when_vacuum_sealed = True   # Indicates exit if vacuum is sealed.

    # Print the velocity command details before publishing.
    print("Publishing CartesianVelocityControllerExecutionRequest with the following command:")
    print("  Timestamp: ", msg.timestamp)
    print("  UUID: ", msg.uuid)
    print("  Robot Type (value): ", msg.robot_type.value)
    print("  Twist frame: ", msg.v_end_effector.frame_expressed_in)
    print("  Linear Velocity (v_xyz): ", msg.v_end_effector.v_xyz)
    print("  Angular Velocity (w_xyz): ", msg.v_end_effector.w_xyz)
    print("  End Conditions:")
    print("    should_exit_when_vacuum_sealed: ", msg.should_exit_when_vacuum_sealed)
    print("    should_failexit_on_zmin: ", msg.should_failexit_on_zmin, "with zmin =", msg.zmin)
    print("    should_failexit_on_duration: ", msg.should_failexit_on_duration, "with max_duration =", msg.max_duration)

    # Encode and publish the message.
    encoded_msg = msg.encode()
    lcm.Publish(channel, encoded_msg)
    print("Published CartesianVelocityControllerExecutionRequest")

if __name__ == "__main__":
    publish_cartesian_velocity_request()
