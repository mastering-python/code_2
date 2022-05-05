>>> import abc


>>> class Plugins(abc.ABCMeta):
...     plugins = dict()
...
...     def __new__(metaclass, name, bases, namespace):
...         cls = abc.ABCMeta.__new__(metaclass, name, bases,
...                                   namespace)
...         if isinstance(cls.name, str):
...             metaclass.plugins[cls.name] = cls
...         return cls
...
...     @classmethod
...     def get(cls, name):
...         return cls.plugins[name]


>>> class PluginBase(metaclass=Plugins):
...     @property
...     @abc.abstractmethod
...     def name(self):
...         raise NotImplemented()


>>> class PluginA(PluginBase):
...     name = 'a'


>>> class PluginB(PluginBase):
...     name = 'b'


>>> Plugins.get('a')
<class '...PluginA'>

>>> Plugins.plugins
{'a': <class '...PluginA'>,
 'b': <class '...PluginB'>}
