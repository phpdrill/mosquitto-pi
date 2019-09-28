# mosquitto-pi

A very simplistic, lightweight Raspberry Pi MQTT client.

**Prerequisites**

Please create two files: things.things and config.txt, copied over from the respective .example files.

The things.things file has a openHAB like syntax.

**Usage**

`python main.py`

**Abilities**

Type switch: Listen to on and off commands.

Type number: Sends the current temperature every 5 seconds.