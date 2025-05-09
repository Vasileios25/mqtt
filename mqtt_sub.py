import sys
import paho.mqtt.client as paho

def message_handling(client, userdata, msg):
    print(f"{msg.topic}: {msg.payload.decode()}")

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")

client = paho.Client()
client.on_message = message_handling
client.on_connect = on_connect  # Handle connection

if client.connect("localhost", 1883, 60) != 0:
    print("Couldn't connect to the mqtt broker")
    sys.exit(1)

client.subscribe("test_topic")

try:
    print("Press CTRL+C to exit...")
    client.loop_forever()
except Exception as e:
    print(f"Caught an Exception: {e}")
finally:
    print("Disconnecting from the MQTT broker")
    client.disconnect()
