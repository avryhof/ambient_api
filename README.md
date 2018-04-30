Ambient API
==========================

Python Module to access the Ambient Weather API

## Classes
There are two classes implemented in this module.

##### AmbientAPI
This is the base APIthat youinitialize in your code.

```python
from ambientapi import AmbientAPI

api = AmbientAPI()
``` 
This class takes care of authenticating to, and sending calls to the API.  It can be expanded as needed in the future.

##### AmbientWeatherStation
This class represents a single Weather Station.  When you ask AmbientAPI for a list of devices,
it returns a list of AmbientWeatherStations, and from this class, you can query the weather station itself.

```python
devices = api.get_devices()

device = devices[0]

print(device.get_data())
```

Learn more about the Ambient Weather API at []https://ambientweather.docs.apiary.io/#