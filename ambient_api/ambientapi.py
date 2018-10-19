import datetime

import requests

from ambient_api import settings


class AmbientWeatherStation:
    """
    This class represents a single weather station.
    """
    api_instance = None
    mac_address = None
    last_data = {}
    info = {
        'name': 'Weather Station'
    }

    def __init__(self, api_instance, device_dict):
        self.api_instance = api_instance
        self.mac_address = device_dict.get('macAddress', None)
        self.last_data = device_dict.get('lastData', {})
        self.info = device_dict.get('info', {})

    def __str__(self):

        return '%s@%s' % (self.info.get('name'), self.mac_address)

    @staticmethod
    def convert_datetime(datetime_object):
        try:
            posix_timestamp = datetime_object.timestamp()

        except AttributeError:
            epoch = datetime.datetime.fromtimestamp(0)
            posix_timestamp = (datetime_object - epoch).total_seconds()

        return int(posix_timestamp * 1000.0)

    def current_time(self):

        return self.convert_datetime(datetime.datetime.now())

    def get_data(self, **kwargs):
        """
        Get the data for a specific device for a specific end date

        Keyword Arguments:
            limit - max 288
            end_date - is Epoch in milliseconds

        :return:
        """
        limit = int(kwargs.get('limit', 288))
        end_date = kwargs.get('end_date', self.current_time())

        if isinstance(end_date, datetime.datetime):
            end_date = self.convert_datetime(end_date)

        if self.mac_address is not None:
            service_address = 'devices/%s' % self.mac_address

            data = dict(
                limit=limit,
                endDate=end_date
            )

            return self.api_instance.api_call(service_address, **data)


class AmbientAPI:
    endpoint = None
    api_key = None
    application_key = None
    client = requests

    def __init__(self, **kwargs):
        http_client = kwargs.get('http_client', requests)

        self.client = http_client
        self.endpoint = getattr(settings, 'AMBIENT_ENDPOINT', None)
        self.api_key = getattr(settings, 'AMBIENT_API_KEY', None)
        self.application_key = getattr(settings, 'AMBIENT_APPLICATION_KEY', None)

    def api_call(self, service, **kwargs):
        retn = {}

        target_url = '%s/%s' % (self.endpoint, service)

        params = {
            'applicationKey': self.application_key,
            'apiKey': self.api_key
        }

        for kwarg_k, kwarg_v in kwargs.items():
            params.update({kwarg_k: kwarg_v})

        res = self.client.get(target_url, params, verify=True)

        if res.status_code == 200:
            retn = res.json()

        return retn

    def get_devices(self):
        """
        Get all devices

        :return:
            A list of AmbientWeatherStation instances.
        """
        retn = []
        for device in self.api_call('devices'):
            retn.append(AmbientWeatherStation(self, device))

        return retn
