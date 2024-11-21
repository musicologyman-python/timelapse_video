import csv
from datetime import datetime, timedelta

from icecream import ic

start_date = datetime(2024, 10, 5)

def get_timestamp(dt: datetime):
    return {'date': dt.strftime('%Y-%m-%d'), 
            'posix timestamp': int(dt.timestamp())}

def write_timestamps(start_date: datetime, end_date: datetime, 
                     increment=timedelta(days=1)):
    with open('timestamps.csv', mode='w', encoding='utf-8-sig') as fp:
        writer = csv.DictWriter(fp, fieldnames=['date', 'posix timestamp'])
        writer.writeheader()
        current_date = start_date
        while current_date < end_date:
            row = get_timestamp(current_date)
            ic(current_date, row)
            writer.writerow(row)
            current_date += increment

def main():
    start_date = datetime(2024, 10, 5)
    end_date = datetime(2024, 12, 31)
    write_timestamps(start_date, end_date)

if __name__ == '__main__':
    main()
