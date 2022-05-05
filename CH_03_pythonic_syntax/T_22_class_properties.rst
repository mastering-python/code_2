>>> class SomeClass:
...     class_list = []
...
...     def __init__(self):
...         self.instance_list = []

>>> SomeClass.class_list.append('from class')
>>> instance = SomeClass()
>>> instance.class_list.append('from instance')
>>> instance.instance_list.append('from instance')

>>> SomeClass.class_list
['from class', 'from instance']
>>> SomeClass.instance_list
Traceback (most recent call last):
...
AttributeError: ... 'SomeClass' has no attribute 'instance_list'

>>> instance.class_list
['from class', 'from instance']
>>> instance.instance_list
['from instance']


>>> class Parent:
...     pass


>>> class Child(Parent):
...     pass


>>> Parent.parent_property = 'parent'
>>> Child.parent_property
'parent'

>>> Child.parent_property = 'child'
>>> Parent.parent_property
'parent'
>>> Child.parent_property
'child'

>>> Child.child_property = 'child'
>>> Parent.child_property
Traceback (most recent call last):
...
AttributeError: ... 'Parent' has no attribute 'child_property'
