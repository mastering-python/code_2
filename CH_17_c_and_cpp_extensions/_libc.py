import platform
from ctypes import cdll

__all__ = 'libc'

if platform.system() == 'Windows':
    libc = cdll.msvcrt
elif platform.system() == 'Darwin':
    libc = cdll.LoadLibrary('libc.dylib')
else:
    libc = cdll.LoadLibrary('libc.so.6')
