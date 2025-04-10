#!/usr/bin/env python

import time
import threading
from pydrake.lcm import DrakeLcm
from lcm_azalea.VacuumControllerExecutionRequest import VacuumControllerExecutionRequest

def publish_vacuum_controller_request(action_input):
    """
    Publish a VacuumControllerExecutionRequest LCM message based on the action input.
    Valid inputs: 'on', 'turn on', '1' (to turn on) or 'off', 'turn off', '0' (to turn off).
    """
    # Create an LCM publisher.
    lcm = DrakeLcm()
    channel = "VACUUM_CONTROLLER_EXECUTION_CHANNEL"
    
    # Create and populate the VacuumControllerExecutionRequest message.
    msg = VacuumControllerExecutionRequest()
    user_choice = action_input.strip().lower()
    if user_choice in ['on', 'turn on', '1']:
        msg.action = VacuumControllerExecutionRequest.TURN_ON
    elif user_choice in ['off', 'turn off', '0']:
        msg.action = VacuumControllerExecutionRequest.TURN_OFF
    else:
        print("Invalid input. Please enter 'on' or 'off'.")
        return

    # Display message details before publishing.
    print("Publishing VacuumControllerExecutionRequest with the following details:")
    print("  Timestamp:", msg.timestamp)
    print("  UUID:", msg.uuid)
    print("  Action:", "TURN_ON" if msg.action == VacuumControllerExecutionRequest.TURN_ON else "TURN_OFF")
    
    # Encode and publish the message.
    encoded_msg = msg.encode()
    lcm.Publish(channel, encoded_msg)
    print("Published VacuumControllerExecutionRequest on channel:", channel)

def wait_for_exit(stop_flag):
    """
    Wait for the user to press Enter. Once Enter is pressed, update the shared flag.
    """
    input("Press Enter to stop the loop...\n")
    stop_flag[0] = True

if __name__ == "__main__":
    # A mutable flag stored in a list so it can be updated in the thread.
    stop_flag = [False]
    
    # Start a background thread that waits for the user to press Enter.
    threading.Thread(target=wait_for_exit, args=(stop_flag,), daemon=True).start()
    
    # Main loop: turn the vacuum on, wait, then turn the vacuum off.
    while not stop_flag[0]:
        publish_vacuum_controller_request("on")
        time.sleep(5)
        publish_vacuum_controller_request("off")
        time.sleep(5)
    
    print("Loop stopped. Exiting script.")
