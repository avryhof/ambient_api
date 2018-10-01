import pprint

from ambient_api.ambientapi import AmbientAPI

weather = AmbientAPI()

devices = weather.get_devices()

for device in devices:
    print(str(device))

    pprint.pprint(device.last_data)

    pprint.pprint(device.get_data())

