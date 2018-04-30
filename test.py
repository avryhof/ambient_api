import pprint

from ambientapi import AmbientAPI

weather = AmbientAPI()

devices = weather.get_devices()

for device in devices:
    print(str(device))

    pprint.pprint(device.last_data)

    pprint.pprint(device.get_data())

