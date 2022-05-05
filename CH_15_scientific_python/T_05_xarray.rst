>>> import re
>>> import io
>>> import pandas as pd

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

>>> data = re.sub(r'\[.+?\]', '', data)
>>> df = pd.read_table(io.StringIO(data), dtype=dict(Version=str))
>>> df['Release date'] = pd.to_datetime(df['Release date'])

# The code above is copied from T_03_pandas.rst

# The common shorthand for xarray is xr

>>> import xarray as xr

>>> ds = xr.Dataset.from_dataframe(df)

# For reference, the pandas version of the groupby
df.groupby([df['Release date'].dt.month])['Version'].count()

>>> ds.groupby('Release date.month').count()['Version']
<xarray.DataArray 'Version' (month: 10)>
array([2, 2, 1, 2, 3, 1, 4, 8, 1, 3])
Coordinates:
  * month    (month) int64 1 2 3 4 6 7 9 10 11 12

#################################################################

>>> import xarray as xr
>>> import numpy as np

>>> points = np.arange(27).reshape((3, 3, 3))
>>> triangles = np.arange(27).reshape((3, 3, 3))
>>> ds = xr.Dataset(dict(
...     triangles=(['p0', 'p1', 'p2'], triangles),
... ), coords=dict(
...     points=(['x', 'y', 'z'], points),
... ))

>>> ds
<xarray.Dataset>
Dimensions:    (p0: 3, p1: 3, p2: 3, x: 3, y: 3, z: 3)
Coordinates:
    points     (x, y, z) int64 0 1 2 3 4 5 ... 21 22 23 24 25 26
Dimensions without coordinates: p0, p1, p2, x, y, z
Data variables:
    triangles  (p0, p1, p2) int64 0 1 2 3 4 ... 21 22 23 24 25 26
