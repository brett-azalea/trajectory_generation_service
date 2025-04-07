from pydrake.lcm import DrakeLcm
from lcm_messages.lcmt_int_value import lcmt_int_value

def subscriber_example():
    lcm = DrakeLcm()
    channel_name = "INTEGER_CHANNEL"
    
    def callback(raw_message):
        try:
            message = lcmt_int_value.decode(raw_message)
            print(f"Received: value={message.value}, timestamp={message.timestamp}")
        except Exception as e:
            print(f"Error decoding message: {e}")
    
    lcm.Subscribe(channel=channel_name, handler=callback)
    print(f"Subscribed to channel: {channel_name}")
    print("Waiting for messages... (Press Ctrl+C to stop)")
    
    try:
        while True:
            lcm.HandleSubscriptions(100)
    except KeyboardInterrupt:
        print("\nSubscriber stopped by user")

if __name__ == "__main__":
    subscriber_example()