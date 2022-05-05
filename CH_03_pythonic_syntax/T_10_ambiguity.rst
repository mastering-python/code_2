>>> fh_a = open('spam', 'w', -1, None, None, '\n')
>>> fh_b = open(file='spam', mode='w', buffering=-1, newline='\n')

>>> filename = 'spam'
>>> mode = 'w'
>>> buffers = -1
>>> fh_b = open(filename, mode, buffers, newline='\n')
