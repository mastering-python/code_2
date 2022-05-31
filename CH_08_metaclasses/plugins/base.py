import re
import abc
import pathlib
import importlib


CURRENT_FILE = pathlib.Path(__file__)
PLUGINS_DIR = CURRENT_FILE.parent
MODULE_NAME_RE = re.compile('[a-z][a-z0-9_]*', re.IGNORECASE)


class Plugins(abc.ABCMeta):

    plugins = dict()

    def __new__(metaclass, name, bases, namespace):
        cls = abc.ABCMeta.__new__(
            metaclass, name, bases, namespace)
        metaclass.plugins[name.lower()] = cls
        return cls

    @classmethod
    def get(cls, name):
        return cls.plugins[name]


class Plugin(metaclass=Plugins):
    pass


class PluginsOnDemand(Plugins):

    @classmethod
    def get(cls, name):
        if name not in cls.plugins:
            print('Loading plugins from plugins.%s' % name)
            importlib.import_module('plugins.%s' % name)
        return cls.plugins[name]


class PluginsThroughConfiguration(PluginsOnDemand):

    @classmethod
    def load(cls, *plugin_names):
        for plugin_name in plugin_names:
            cls.get(plugin_name)


class PluginsThroughFilesystem(PluginsThroughConfiguration):

    @classmethod
    def autoload(cls):
        for filename in PLUGINS_DIR.glob('*.py'):
            # Skip __init__.py and other non-plugin files
            if not MODULE_NAME_RE.match(filename.stem):
                continue

            # Skip this file
            if filename == CURRENT_FILE:
                continue

            # Load the plugin
            cls.get(filename.stem)
