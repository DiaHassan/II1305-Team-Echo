import sys
import logging
from get_ads import get_ads, date
from database import load_all
from settings import LOG_LEVEL, LOG_DATE_FORMAT, LOG_FORMAT


# Logging
log = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=LOG_LEVEL, format=LOG_FORMAT, datefmt=LOG_DATE_FORMAT)


# Main script
if __name__ == '__main__':
    all_ads = get_ads()
    list = load_all(all_ads)
    log.info(f'Loaded {len(all_ads)}. Timestamp: {date}')