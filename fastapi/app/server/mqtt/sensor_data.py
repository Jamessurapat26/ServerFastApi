from fastapi import APIRouter 
#fastapi_mqtt
from fastapi_mqtt.fastmqtt import FastMQTT
from fastapi_mqtt.config import MQTTConfig

mqtt_config = MQTTConfig(host = "192.168.1.2",
    port= 1883,
    keepalive = 60,
    username="TGR_GROUP16",
    password="ED370J")

fast_mqtt = FastMQTT(config=mqtt_config)

router = APIRouter()

fast_mqtt.init_app(router)

from server.database import (
    add_water,
)
from server.models.water import (
    ErrorResponseModel,
    ResponseModel,
    WaterSchema,
)

@fast_mqtt.on_connect()
def connect(client, flags, rc, properties):
    fast_mqtt.client.subscribe("/TGR_16") #subscribing mqtt topic
    print("Connected: ", client, flags, rc, properties)

@fast_mqtt.on_message()
async def message(client, topic, payload, qos, properties):
    print("Received message: ",topic, payload.decode(), qos, properties)

@fast_mqtt.subscribe("/TGR_16")
async def message_to_topic(client, topic, payload, qos, properties):
    print("Received message to specific topic: ", topic, payload.decode(), qos, properties)

@fast_mqtt.on_disconnect()
def disconnect(client, packet, exc=None):
    print("Disconnected")

@fast_mqtt.on_subscribe()
def subscribe(client, mid, qos, properties):
    print("subscribed", client, mid, qos, properties)


# @router.get("/", response_description="test publish to mqtt")
# async def publish_hello():
#     fast_mqtt.publish("/mqtt", "Hello, world") #publishing mqtt topic
#     return {"result": True,"message":"Published" }

@fast_mqtt.on_connect()
def connect(client, flags, rc, properties):
    fast_mqtt.client.subscribe("/TGR_16") #subscribing mqtt topic
    print("Connected: ", client, flags, rc, properties)

@router.get("/", response_description="test publish to mqtt")
async def publish_hello():
    fast_mqtt.publish("/TGR_16", "Hello TGR_16") #publishing mqtt topic
    return {"result": True,"message":"Published" }