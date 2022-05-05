>>> import operator
>>> import itertools

>>> words = ['aa', 'ab', 'ba', 'bb', 'ca', 'cb', 'cc']

# Gets the first element from the iterable

>>> getter = operator.itemgetter(0)

>>> for group, items in itertools.groupby(words, key=getter):
...     print(f'group: {group}, items: {list(items)}')
group: a, items: ['aa', 'ab']
group: b, items: ['ba', 'bb']
group: c, items: ['ca', 'cb', 'cc']

------------------------------------------------------------

>>> import operator
>>> import itertools

>>> words = ['aa', 'bb', 'ca', 'ab', 'ba', 'cb', 'cc']

# Gets the first element from the iterable

>>> getter = operator.itemgetter(0)

>>> for group, items in itertools.groupby(words, key=getter):
...     print(f'group: {group}, items: {list(items)}')
group: a, items: ['aa']
group: b, items: ['bb']
group: c, items: ['ca']
group: a, items: ['ab']
group: b, items: ['ba']
group: c, items: ['cb', 'cc']
