import plugins

plugins.PluginsThroughConfiguration.load(
    'a',
    'b',
)

print('After load')
print(plugins.PluginsThroughConfiguration.get('a'))
print(plugins.PluginsThroughConfiguration.get('a'))
