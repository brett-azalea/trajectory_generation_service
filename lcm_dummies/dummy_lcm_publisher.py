from pydrake.lcm import DrakeLcm
from lcm_messages.lcmt_int_value import lcmt_int_value 
import time

def publish_integer_periodically(period_seconds=1.0):
    lcm = DrakeLcm()
    
    channel_name = "INTEGER_CHANNEL"
    
    counter = 0
    
    print(f"Starting periodic publishing every {period_seconds} seconds on channel: {channel_name}")
    
    try:
        while True:
            message = lcmt_int_value()
            
            message.value = counter
            message.timestamp = int(time.time() * 1000)  # Current time in milliseconds
            
            encoded_message = message.encode()
            lcm.Publish(channel=channel_name, buffer=encoded_message)
            
            print(f"Published integer value: {message.value} at timestamp: {message.timestamp}")
            
            counter += 1
            
            time.sleep(period_seconds)
            
    except KeyboardInterrupt:
        print("\nStopped by user (Ctrl+C)")

if __name__ == "__main__":
    publish_integer_periodically(period_seconds=1.0)