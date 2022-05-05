>>> import copy

>>> x = [[1], [2, 3]]
>>> y = x.copy()
>>> z = copy.deepcopy(x)

>>> x.append('a')
>>> x[0].append(x)

>>> x
[[1, [...]], [2, 3], 'a']
>>> y
[[1, [...]], [2, 3]]
>>> z
[[1], [2, 3]]


>>> def append(list_=[], value='value'):
...    list_.append(value)
...    return list_

>>> append(value='a')
['a']
>>> append(value='b')
['a', 'b']


>>> def append(list_=None, value='value'):
...    if list_ is None:
...        list_ = []
...    list_.append(value)
...    return list_

>>> append(value='a')
['a']
>>> append(value='b')
['b']
