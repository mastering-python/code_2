>>> timestamp = 12345
>>> filename = f'{timestamp}.csv'

>>> import datetime

>>> timestamp = 12345

>>> if isinstance(timestamp, datetime.datetime):
...     filename = f'{timestamp}.csv'
... else:
...     raise TypeError(f'{timestamp} is not a valid datetime')
Traceback (most recent call last):
...
TypeError: 12345 is not a valid datetime



>>> import datetime

>>> timestamp = datetime.date(2000, 10, 5)
>>> filename = f'{timestamp}.csv'
>>> print(f'Filename from date: {filename}')
Filename from date: 2000-10-05.csv

>>> timestamp = '2000-10-05'
>>> filename = f'{timestamp}.csv'
>>> print(f'Filename from str: {filename}')
Filename from str: 2000-10-05.csv
