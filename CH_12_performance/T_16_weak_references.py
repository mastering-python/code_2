import gc
import weakref


class SomeClass(object):

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<%s: %s>' % (self.__class__.__name__, self.name)


def print_mem(message):
    print(message)
    for object_ in gc.get_objects():
        if isinstance(object_, SomeClass):
            print('\t', object_, gc.get_referents(object_))


# Create the objects
a = SomeClass('a')
b = SomeClass('b')

# Add some weak circular references
a.b = weakref.ref(a)
b.a = weakref.ref(b)

print_mem('Objects in memory before del:')

# Remove the objects
del a
del b

# See if the objects are still there
print_mem('Objects in memory after del:')
