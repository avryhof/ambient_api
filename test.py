import datetime
import pprint

from ambient_api.ambientapi import AmbientAPI

weather = AmbientAPI()

devices = weather.get_devices()

for device in devices:
    print('Device')
    print(str(device))

    print('Last Data')
    pprint.pprint(device.last_data)

    print('Get Data')
    pprint.pprint(device.get_data(end_date=datetime.datetime(year=2018, month=10, day=1)))
