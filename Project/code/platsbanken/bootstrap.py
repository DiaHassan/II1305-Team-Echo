import sys
import logging
import datetime
from get_ads import get_ads, date
from database import load_all, DBConnectionHandler

from settings import LOG_LEVEL, LOG_DATE_FORMAT, LOG_FORMAT, DB_TABLE_NAME, PLACES, OCCUPATIONS, DB_FILE_NAME

log = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=LOG_LEVEL, format=LOG_FORMAT, datefmt=LOG_DATE_FORMAT)

if __name__ == '__main__':
    
    # This is executed once to create the database and 
    # load all ads into it 

    with DBConnectionHandler() as db:
        db.create_db_table()
    log.info(f'Database created: "{DB_FILE_NAME}"')

    all_ads = get_ads()
    load_all(all_ads)
    log.info(f'Loaded {len(all_ads)} into the database table "{DB_TABLE_NAME}". Timestamp: {date}')