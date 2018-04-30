import os

from dotenv import load_dotenv

env_file = os.path.join('.', 'settings.env')
load_dotenv(dotenv_path=env_file)

AMBIENT_ENDPOINT = 'https://api.ambientweather.net/v1'
AMBIENT_APPLICATION_KEY = os.environ['AMBIENT_APPLICATION_KEY']
AMBIENT_API_KEY = os.environ['AMBIENT_API_KEY']
