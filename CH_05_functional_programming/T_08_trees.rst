>>> import json
>>> import functools
>>> import collections

>>> def tree():
...     return collections.defaultdict(tree)

# Build the tree:

>>> taxonomy = tree()
>>> reptilia = taxonomy['Chordata']['Vertebrata']['Reptilia']
>>> reptilia['Squamata']['Serpentes']['Pythonidae'] = [
...     'Liasis', 'Morelia', 'Python']

# The actual contents of the tree

>>> print(json.dumps(taxonomy, indent=4))
{
    "Chordata": {
        "Vertebrata": {
            "Reptilia": {
                "Squamata": {
                    "Serpentes": {
                        "Pythonidae": [
                            "Liasis",
                            "Morelia",
                            "Python"
                        ]
                    }
                }
            }
        }
    }
}


# Let's build the lookup function

>>> import operator

>>> def lookup(tree, path):
...     # Split the path for easier access
...     path = path.split('.')
...
...     # Use `operator.getitem(a, b)` to get `a[b]`
...     # And use reduce to recursively fetch the items
...     return functools.reduce(operator.getitem, path, tree)


>>> path = 'Chordata.Vertebrata.Reptilia.Squamata.Serpentes'
>>> dict(lookup(taxonomy, path))
{'Pythonidae': ['Liasis', 'Morelia', 'Python']}

# The path we wish to get

>>> path = 'Chordata.Vertebrata.Reptilia.Squamata'
>>> lookup(taxonomy, path).keys()
dict_keys(['Serpentes'])

------------------------------------------------------------------------------

>>> fold_left = lambda iterable, initializer=None: functools.reduce(
...     lambda x, y: function(x, y),
...     iterable,
...     initializer,
... )

>>> fold_right = lambda iterable, initializer=None: functools.reduce(
...     lambda x, y: function(y, x),
...     reversed(iterable),
...     initializer,
... )

