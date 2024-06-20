import pprint
import time

from ambient_api.ambientapi import AmbientAPI

weather = AmbientAPI(log_level='CONSOLE')


def test_endpoint():
    assert weather.endpoint == 'https://rt.ambientweather.net/v1'


devices = weather.get_devices()


def test_devices():
    assert len(devices) == 0


for device in devices:
    # Wait two seconds between requests so we don't get a 429 response.
    # https://ambientweather.docs.apiary.io/#introduction/rate-limiting
    # This probably won't happen much in real world situations.
    time.sleep(2)
    print('Device')
    print((str(device)))

    print('Last Data')
    pprint.pprint(device.last_data)

    print('Get Data')
    pprint.pprint(device.get_data())
