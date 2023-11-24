from fastapi import APIRouter
from fastapi_mqtt.fastmqtt import FastMQTT
from fastapi_mqtt.config import MQTTConfig

import asyncio

mqtt_config = MQTTConfig(
    host="192.168.1.2",
    port=1883,
    keepalive=60,
    username="TGR_GROUP16",
    password="ED370J"
)

fast_mqtt = FastMQTT(config=mqtt_config)
router = APIRouter()
fast_mqtt.init_app(router)

response_received = asyncio.Event()

@fast_mqtt.on_connect()
def connect(client, flags, rc, properties):
    fast_mqtt.client.subscribe("/TGR_16")  # subscribing mqtt topic
    print("Connected: ", client, flags, rc, properties)

@fast_mqtt.on_message()
async def message(client, topic, payload, qos, properties):
    print("Received message: ", topic, payload.decode(), qos, properties)
    # Check if the received message is a response to the "capture" command
    if payload.decode() == "capture_response":
        response_received.set()

@fast_mqtt.on_disconnect()
def disconnect(client, packet, exc=None):
    print("Disconnected")

@router.get("/", response_description="test capture command")
async def publish_capture():
    global response_received
    response_received.clear()
    
    # Publish the "capture" message
    fast_mqtt.publish("/TGR_16", "capture")
    print("Capture message published")

    try:
        # Wait for a response for 5 seconds
        await asyncio.wait_for(response_received.wait(), timeout=5)
        print("Response received", response_received)
    except asyncio.TimeoutError:
        print("Timeout: No response received", response_received)

    # Check if a response was received
    if response_received.is_set():
        return {"result": True, "message": "Capture successful"}
    else:
        return {"result": False, "message": "Capture failed: No response received"}

@router.get("/capture", response_description="test publish to mqtt")
async def test_capture_command():
    # Simulate a delay and then publish a capture response
    await asyncio.sleep(2)
    fast_mqtt.publish("/TGR_16", "capture")
    return {"result": True, "message": "Capture published"}

@router.get("/test", response_description="test publish to mqtt")
async def publish_hello():
    global response_received
    response_received.clear()

    # Debugging output
    print("About to publish 'capture' message")

    # Publish the "capture" message
    fast_mqtt.publish("/TGR_16", "capture")
    print("Capture message published")