# Simple formatting

>>> name = 'Rick'

>>> 'Hi %s' % name
'Hi Rick'

>>> 'Hi {}'.format(name)
'Hi Rick'


>>> value = 1 / 3

>>> '%.2f' % value
'0.33'

>>> '{:.2f}'.format(value)
'0.33'


>>> name = 'Rick'
>>> value = 1 / 3

>>> 'Hi {0}, value: {1:.3f}. Bye {0}'.format(name, value)
'Hi Rick, value: 0.333. Bye Rick'


# Named variables

>>> name = 'Rick'

>>> 'Hi %(name)s' % dict(name=name)
'Hi Rick'

>>> 'Hi {name}'.format(name=name)
'Hi Rick'

>>> f'Hi {name}'
'Hi Rick'

>>> 'Hi {name}'.format(**globals())
'Hi Rick'

# Arbitrary expressions

## Accessing dict items

>>> username = 'wolph'
>>> a = 123
>>> b = 456
>>> some_dict = dict(a=a, b=b)

>>> f'''a: {some_dict['a']}'''
'a: 123'

>>> f'''sum: {some_dict['a'] + some_dict['b']}'''
'sum: 579'

## Python expressions, specifically an inline if statement

>>> f'if statement: {a if a > b else b}'
'if statement: 456'

## Function calls

>>> f'min: {min(a, b)}'
'min: 123'

>>> f'Hi {username}. And in uppercase: {username.upper()}'
'Hi wolph. And in uppercase: WOLPH'

## Loops

>>> f'Squares: {[x ** 2 for x in range(5)]}'
'Squares: [0, 1, 4, 9, 16]'



