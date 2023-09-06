import logging, time, csv, sys, datetime
from dalybms import DalyBMS


address = 4 # https://github.com/dreadnought/python-daly-bms/blob/main/bin/daly-bms-cli#L71C4-L71C16
retry = 5

bms = DalyBMS(request_retries=retry, address=address, logger=logging.getLogger())
bms.connect(device="/dev/ttyUSB0")

bms2 = DalyBMS(request_retries=retry, address=address, logger=logging.getLogger())
bms2.connect(device="/dev/ttyUSB1")

csv_writer = csv.writer(sys.stdout)
csv_writer2 = csv.writer(sys.stderr)

while True:
    row = list(bms.get_soc().values()) + list(bms2.get_soc().values())
    row = [datetime.datetime.now().isoformat()] + row
    csv_writer.writerow(row)
    csv_writer2.writerow(row)
    time.sleep(5)


