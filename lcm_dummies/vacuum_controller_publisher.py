#!/usr/bin/env python

import argparse
import time
from pydrake.lcm import DrakeLcm
from lcm_azalea.VacuumControllerExecutionRequest import VacuumControllerExecutionRequest

def publish_vacuum_controller_request(action_input):
    # Create an LCM publisher.
    lcm = DrakeLcm()
    channel = "VACUUM_CONTROLLER_EXECUTION_CHANNEL"
    
    # Create and populate the VacuumControllerExecutionRequest message.
    msg = VacuumControllerExecutionRequest()
    msg.timestamp = int(time.time() * 1000)  # Current time in milliseconds.
    msg.uuid = "unique-vacuum-request-id"      # A unique identifier for the request.
    
    # Set action based on user input.
    # Accepts common variations: "on", "turn on", "1" for turning on; "off", "turn off", "0" for turning off.
    user_choice = action_input.strip().lower()
    if user_choice in ['on', 'turn on', '1']:
        msg.action = VacuumControllerExecutionRequest.TURN_ON
    elif user_choice in ['off', 'turn off', '0']:
        msg.action = VacuumControllerExecutionRequest.TURN_OFF
    else:
        print("Invalid input. Please enter 'on' or 'off'.")
        return

    # Print the message details before publishing.
    print("Publishing VacuumControllerExecutionRequest with the following details:")
    print("  Timestamp:", msg.timestamp)
    print("  UUID:", msg.uuid)
    print("  Action:", "TURN_ON" if msg.action == VacuumControllerExecutionRequest.TURN_ON else "TURN_OFF")
    
    # Encode and publish the message.
    encoded_msg = msg.encode()
    lcm.Publish(channel, encoded_msg)
    print("Published VacuumControllerExecutionRequest on channel:", channel)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Send a Vacuum Controller Execution Request (on/off) via LCM."
    )
    parser.add_argument(
        "action",
        help="Specify the vacuum action. Acceptable values: 'on', 'turn on', '1', 'off', 'turn off', or '0'.",
        choices=["on", "turn on", "1", "off", "turn off", "0"]
    )
    args = parser.parse_args()
    
    publish_vacuum_controller_request(args.action)
