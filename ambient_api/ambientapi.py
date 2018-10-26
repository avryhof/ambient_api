import datetime
import logging

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
        retn = '%s@%s' % (self.info.get('name'), self.mac_address)
        self.api_instance.log(retn)

        return retn

    def convert_datetime(self, datetime_object):
        try:
            posix_timestamp = datetime_object.timestamp()

        except AttributeError:
            epoch = datetime.datetime(year=1969, month=12, day=31, hour=19, minute=0, second=0)
            self.api_instance.log('EPOCH:')
            self.api_instance.log(epoch)

            posix_timestamp = (datetime_object - epoch).total_seconds()

        self.api_instance.log('POSIX TIMESTAMP:')
        self.api_instance.log(posix_timestamp)

        return int(posix_timestamp * 1000.0)

    def current_time(self):
        retn = self.convert_datetime(datetime.datetime.now())
        self.api_instance.log(retn)

        return retn

    def get_data(self, **kwargs):
        """
        Get the data for a specific device for a specific end date

        Keyword Arguments:
            limit - max 288
            end_date - is Epoch in milliseconds

        :return:
        """
        limit = int(kwargs.get('limit', 288))
        end_date = kwargs.get('end_date', False)

        if end_date and isinstance(end_date, datetime.datetime):
            end_date = self.convert_datetime(end_date)

        if self.mac_address is not None:
            service_address = 'devices/%s' % self.mac_address
            self.api_instance.log('SERVICE ADDRESS: %s' % service_address)

            data = dict(limit=limit)

            # If endDate is left blank (not passed in), the most recent results will be returned.
            if end_date:
                data.update({'endDate': end_date})

            self.api_instance.log('DATA:')
            self.api_instance.log(data)

            return self.api_instance.api_call(service_address, **data)


class AmbientAPI:
    endpoint = None
    api_key = None
    application_key = None
    client = requests

    log_level = None

    def __init__(self, **kwargs):
        http_client = kwargs.get('http_client', requests)

        self.client = http_client
        self.endpoint = getattr(settings, 'AMBIENT_ENDPOINT', None)
        self.api_key = getattr(settings, 'AMBIENT_API_KEY', None)
        self.application_key = getattr(settings, 'AMBIENT_APPLICATION_KEY', None)

        default_log_level = getattr(settings, 'AMBIENT_LOG_LEVEL', None)
        self.log_level = kwargs.get('log_level', default_log_level)
        default_log_file = getattr(settings, 'AMBIENT_LOG_FILE', None)
        self.log_file = kwargs.get('log_file', default_log_file)

    def log(self, message):
        if self.log_level:
            log_level = self.log_level.lower()

            if self.log_file and log_level != 'console':
                logging.basicConfig(filename=self.log_file, level=getattr(logging, log_level.upper(), 'ERROR'))

            if log_level == 'debug':
                logging.debug(message)
            if log_level == 'info':
                logging.info(message)
            if log_level == 'warning':
                logging.warning(message)
            if log_level == 'error':
                logging.error(message)
            if log_level == 'critical':
                logging.critical(message)
            if log_level == 'console':
                print(message)

    def api_call(self, service, **kwargs):
        retn = {}

        target_url = '%s/%s' % (self.endpoint, service)
        self.log('TARGET URL: %s' % target_url)

        params = {
            'applicationKey': self.application_key,
            'apiKey': self.api_key
        }

        for kwarg_k, kwarg_v in kwargs.items():
            params.update({kwarg_k: kwarg_v})

        # Remove sensitive parameters from log
        if self.log_level:
            log_params = params.copy()
            log_params['applicationKey'] = '[secure]'
            log_params['apiKey'] = '[secure]'
            self.log('PARAMS:')
            self.log(log_params)

        res = self.client.get(target_url, params, verify=True)
        self.log('RESPONSE:')
        self.log(res)

        if res.status_code == 200:
            retn = res.json()
            self.log('RETURN DATA:')
            self.log(retn)

        if res.status_code == 429:
            self.log('RATE LIMIT EXCEEDED')

        return retn

    def get_devices(self):
        """
        Get all devices

        :return:
            A list of AmbientWeatherStation instances.
        """
        retn = []
        api_devices = self.api_call('devices')

        self.log('DEVICES:')
        self.log(api_devices)

        for device in api_devices:
            retn.append(AmbientWeatherStation(self, device))

        self.log('DEVICE INSTANCE LIST:')
        self.log(retn)

        return retn
