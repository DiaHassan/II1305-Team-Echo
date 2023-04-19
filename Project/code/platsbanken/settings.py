import logging

# URL and format
BASE_URL = 'https://jobstream.api.jobtechdev.se'
STREAM_URL = f"{BASE_URL}/stream"
DATE_FORMAT = "%Y-%m-%dT%H:%M:%S"


# Logging
LOG_LEVEL = logging.INFO  # Change INFO to DEBUG for verbose logging
LOG_FORMAT = '%(asctime)s  %(levelname)-8s %(message)s'
LOG_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
