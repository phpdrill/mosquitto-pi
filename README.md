# mosquitto-pi

A very simplistic, lightweight Raspberry Pi MQTT client.

**Prerequisites**
Install mosquitto and paho-mqtt.

Please create two files: things.things (has a openHAB like syntax) and config.txt, copied over from the respective .example files.

**Usage**

`python main.py`

**Abilities**

Type switch: Listen to on and off commands.

Type number: Sends the current temperature every 5 seconds.
