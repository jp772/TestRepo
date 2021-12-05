import logging
from datetime import datetime, timezone

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
Log_Format = logging.Formatter('%(levelname)s %(asctime)s - %(message)s')
fh = logging.FileHandler('../tests/Results_Log/logfile.log')

fh.setFormatter(Log_Format)
logger.addHandler(fh)


def log_data_to_logfile(time,record_num,filename, col1, operation, col2, result):
    record_num +=  1
    unixtime = int(time.time())
    time1 = datetime.fromtimestamp(unixtime, tz=timezone.utc)

    with open('../tests/Results_Log/logfile.log','a') as append:

        append.write(f'Time:{time1} - RecordNum:{record_num} - FileName:{filename} - Values:{col1}{operation}{col2} = Results:{result}\n')


    return append

