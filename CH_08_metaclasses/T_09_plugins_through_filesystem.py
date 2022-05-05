import pprint
import plugins

plugins.PluginsThroughFilesystem.autoload()

print('After load')
pprint.pprint(plugins.PluginsThroughFilesystem.plugins)
