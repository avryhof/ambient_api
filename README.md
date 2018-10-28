[![PyPI version](https://badge.fury.io/py/ambient-api.svg)](https://pypi.python.org/pypi/ambient-api)
[![Build Status](https://travis-ci.org/avryhof/ambient_api.svg?branch=master)](https://travis-ci.org/avryhof/ambient_api) 
[![codecov](https://codecov.io/gh/avryhof/ambient_api/branch/master/graph/badge.svg)](https://codecov.io/gh/avryhof/ambient_api)
<a href="https://www.codefactor.io/repository/github/avryhof/ambient_api"><img alt="CodeFactor" src=
   "https://www.codefactor.io/repository/github/avryhof/ambient_api/badge"/></a>

Ambient API
==========================

Python Module to access the Ambient Weather API

## Installation

```bash
pip install ambient_api
```

### Environmental Variables
```bash
AMBIENT_ENDPOINT=https://api.ambientweather.net/v1
AMBIENT_API_KEY='your-api-key-here'
AMBIENT_APPLICATION_KEY='your-application-key-here'
```
Get these values by following [these instructions](https://ambientweather.docs.apiary.io/#introduction/authentication).

## Classes
There are two classes implemented in this module.

### AmbientAPI
This is the base API that you initialize in your code.

```python
from ambient_api import AmbientAPI

api = AmbientAPI()
``` 
This class takes care of authenticating to, and sending calls to the API.  It can be expanded as needed in the future.

### AmbientWeatherStation
This class represents a single Weather Station.  When you ask AmbientAPI for a list of devices,
it returns a list of AmbientWeatherStations, and from this class, you can query the weather station itself.

```python
devices = api.get_devices()

device = devices[0]

print(device.get_data())
```

Learn more about the Ambient Weather API at the [Ambient Weather API Documentation](https://ambientweather.docs.apiary.io/#).

## Also Check Out
* [Ambient APRS](https://github.com/avryhof/ambient_aprs)
