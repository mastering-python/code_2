# A commonly used shorthand for pandas is pd

>>> import pandas as pd
>>> import re
>>> import io

>>> data = '''
... Version\tLatest micro version\tRelease date\tEnd of full support\tEnd of security fixes
... 0.9\t0.9.9[2]\t1991-02-20[2]\t1993-07-29[a][2]
... 1.0\t1.0.4[2]\t1994-01-26[2]\t1994-02-15[a][2]
... 1.1\t1.1.1[2]\t1994-10-11[2]\t1994-11-10[a][2]
... 1.2\t\t1995-04-13[2]\tUnsupported
... 1.3\t\t1995-10-13[2]\tUnsupported
... 1.4\t\t1996-10-25[2]\tUnsupported
... 1.5\t1.5.2[39]\t1998-01-03[2]\t1999-04-13[a][2]
... 1.6\t1.6.1[39]\t2000-09-05[40]\t2000-09[a][39]
... 2.0\t2.0.1[41]\t2000-10-16[42]\t2001-06-22[a][41]
... 2.1\t2.1.3[41]\t2001-04-15[43]\t2002-04-09[a][41]
... 2.2\t2.2.3[41]\t2001-12-21[44]\t2003-05-30[a][41]
... 2.3\t2.3.7[41]\t2003-06-29[45]\t2008-03-11[a][41]
... 2.4\t2.4.6[41]\t2004-11-30[46]\t2008-12-19[a][41]
... 2.5\t2.5.6[41]\t2006-09-19[47]\t2011-05-26[a][41]
... 2.6\t2.6.9[26]\t2008-10-01[26]\t2010-08-24[b][26]\t2013-10-29[26]
... 2.7\t2.7.18[31]\t2010-07-03[31]\t2020-01-01[c][31]
... 3.0\t3.0.1[41]\t2008-12-03[26]\t2009-06-27[48]
... 3.1\t3.1.5[49]\t2009-06-27[49]\t2011-06-12[50]\t2012-06[49]
... 3.2\t3.2.6[51]\t2011-02-20[51]\t2013-05-13[b][51]\t2016-02-20[51]
... 3.3\t3.3.7[52]\t2012-09-29[52]\t2014-03-08[b][52]\t2017-09-29[52]
... 3.4\t3.4.10[53]\t2014-03-16[53]\t2017-08-09[54]\t2019-03-18[a][53]
... 3.5\t3.5.10[55]\t2015-09-13[55]\t2017-08-08[56]\t2020-09-30[55]
... 3.6\t3.6.13[57]\t2016-12-23[57]\t2018-12-24[b][57]\t2021-12[57]
... 3.7\t3.7.10[58]\t2018-06-27[58]\t2020-06-27[b][58]\t2023-06[58]
... 3.8\t3.8.10[59]\t2019-10-14[59]\t2021-05-03[59]\t2024-10[59]
... 3.9\t3.9.5[60]\t2020-10-05[60]\t2022-05[61]\t2025-10[60][61]
... 3.10\t\t2021-10-04[62]\t2023-05[62]\t2026-10[62]
... '''.strip()

# Slightly cleanup data by removing references

>>> data = re.sub(r'\[.+?\]', '', data)

# df is often used as a shorthand for pandas.DataFrame

>>> df = pd.read_table(io.StringIO(data))

# List the columns

>>> df.columns
Index(['Version', ..., 'Release date', ...], dtype='object')

# List the versions:

>>> df['Version']
0     0.9
...
25    3.9
26    3.1
Name: Version, dtype: float64

# Oops... where did Python 3.10 go in the output above? The
conversion to float trimmed the 0 so we need to disable that.

>>> df = pd.read_table(io.StringIO(data), dtype=dict(Version=str))

# Much better, we didn't lose the version info this time

>>> df['Version']
0      0.9
...
25     3.9
26     3.10
Name: Version, dtype: object

# The release date is read as a string by default, so we convert
it to a datetime:

>>> df['Release date'] = pd.to_datetime(df['Release date'])

>>> df['Release date']
0      1991-02-20
...
26     2021-10-04
Name: Release date, dtype: datetime64[ns]

# Let's see which month is the most popular for Python releases.
First we run groupby() on the release month and after that we
run a count() on the version:

>>> df.groupby([df['Release date'].dt.month])['Version'].count()
Release date
1     2
2     2
3     1
4     2
6     3
7     1
9     4
10    8
11    1
12    3
Name: Version, dtype: int64

#################################################################

>>> import pandas as pd
>>> import numpy as np

>>> df = pd.DataFrame(dict(
...     building=['x', 'x', 'y', 'x', 'x', 'y', 'z', 'z', 'z'],
...     rooms=['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c'],
...     hours=[10, 11, 12, 10, 11, 12, 10, 11, 12],
...     
...     temperatures=np.arange(0.0, 9.0),
... ))

>>> df
  building rooms  hours  temperatures
0        x     a     10           0.0
1        x     a     11           1.0
...
7        z     c     11           7.0
8        z     c     12           8.0

>>> pd.pivot_table(
...     df, values='temperatures', index=['rooms'],
...     columns=['hours'], aggfunc=np.mean)
hours   10   11   12
rooms
a      0.0  1.0  2.0
b      3.0  4.0  5.0
c      6.0  7.0  8.0

>>> pd.pivot_table(
...     df, values='temperatures', index=['building', 'rooms'],
...     columns=['hours'], aggfunc=np.mean)
hours            10   11   12
building rooms
x        a      0.0  1.0  NaN
         b      3.0  4.0  NaN
y        a      NaN  NaN  2.0
         b      NaN  NaN  5.0
z        c      6.0  7.0  8.0

>>> df.groupby(pd.Grouper(key='hours')).mean()
       temperatures
hours
10              3.0
11              4.0
12              5.0

#################################################################

>>> import pandas as pd
>>> import numpy as np

>>> df = pd.DataFrame(dict(
...     building=['x', 'x', 'y', 'x', 'x', 'y', 'z', 'z', 'z'],
...     rooms=['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c'],
...     hours=[10, 11, 12, 10, 11, 12, 10, 11, 12],
...     
...     temperatures=np.arange(0.0, 9.0),
... ))

>>> df
  building rooms  hours  temperatures
0        x     a     10           0.0
1        x     a     11           1.0
...
7        z     c     11           7.0
8        z     c     12           8.0

>>> pd.pivot_table(
...     df, values='temperatures', index=['rooms'],
...     columns=['hours'], aggfunc=np.mean)
hours   10   11   12
rooms
a      0.0  1.0  2.0
b      3.0  4.0  5.0
c      6.0  7.0  8.0

>>> pd.pivot_table(
...     df, values='temperatures', index=['building', 'rooms'],
...     columns=['hours'], aggfunc=np.mean)
hours            10   11   12
building rooms
x        a      0.0  1.0  NaN
         b      3.0  4.0  NaN
y        a      NaN  NaN  2.0
         b      NaN  NaN  5.0
z        c      6.0  7.0  8.0

#################################################################

>>> import pandas as pd
>>> import numpy as np

>>> pd_series = pd.Series(np.arange(100))  # [0, 1, 2, ... 99]

# Create a  rolling Window with size 10

>>> window = pd_series.rolling(10)

# Calculate the running mean and ignore the N/A values at the
beginning before the window is full:

>>> window.mean().dropna()
9      4.5
10     5.5
      ...
99    94.5
Length: 91, dtype: float64
