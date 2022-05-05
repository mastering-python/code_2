import gc


class SomeClass(object):

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'<{self.__class__.__name__}: {self.name}'


# Create the objects
a = SomeClass('a')
b = SomeClass('b')

# Add some circular references
a.b = a
b.a = b

# Remove the objects
del a
del b

# See if the objects are still there
print('Before manual collection:')
for object_ in gc.get_objects():
    if isinstance(object_, SomeClass):
        print('\t', object_, gc.get_referents(object_))

print('After manual collection:')
gc.collect()
for object_ in gc.get_objects():
    if isinstance(object_, SomeClass):
        print('\t', object_, gc.get_referents(object_))

print('Thresholds:', gc.get_threshold())
