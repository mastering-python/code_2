>>> import time

>>> a = time.time()
>>> b = time.time()
>>> (b - a) < 0.01
True

------------------------------------------------------------------------------

>>> import datetime

>>> a = datetime.datetime.now()
>>> b = datetime.datetime.now()
>>> str(b - a)  # doctest: +ELLIPSIS
'0:00:00.000...

