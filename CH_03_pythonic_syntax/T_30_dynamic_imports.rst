>>> import importlib

>>> module_name = 'sys'
>>> attribute = 'version_info'

>>> module = importlib.import_module(module_name)
>>> module
<module 'sys' (built-in)>
>>> getattr(module, attribute).major
3
