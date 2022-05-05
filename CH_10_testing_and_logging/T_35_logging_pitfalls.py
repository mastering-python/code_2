import logging


ab = logging.getLogger('a.b')
ab.setLevel(logging.ERROR)
ab.propagate = False
ab.addHandler(logging.StreamHandler())

a = logging.getLogger('a')

ab.error('before setting level')
a.setLevel(logging.CRITICAL)
ab.error('after setting level')
