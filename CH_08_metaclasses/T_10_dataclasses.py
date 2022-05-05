import inspect


class Dataclass(type):

    def _get_signature(namespace):
        # Get the annotations from the class
        annotations = namespace.get('__annotations__', dict())

        # Signatures are immutable so we need to build the
        # parameter list before creating the signature
        parameters = []
        for name, annotation in annotations.items():

            # Create Parameter shortcut for readability
            Parameter = inspect.Parameter

            # Create the parameter with the correct type
            # annotation and default. You could also choose to
            # make the arguments keyword/positional only here
            parameters.append(Parameter(
                name=name,
                kind=Parameter.POSITIONAL_OR_KEYWORD,
                default=namespace.get(name, Parameter.empty),
                annotation=annotation,
            ))

        return inspect.Signature(parameters)

    def _create_init(namespace, signature):
        # If init exists we don't need to do anything
        if '__init__' in namespace:
            return

        # Create the __init__ method and use the signature to
        # process the arguments

        def __init__(self, *args, **kwargs):
            bound = signature.bind(*args, **kwargs)
            bound.apply_defaults()

            for key, value in bound.arguments.items():
                # Convert to the annotation to enforce types
                parameter = signature.parameters[key]
                # Set the casted value
                setattr(self, key, parameter.annotation(value))

        # Override the signature for __init__ so help() works
        __init__.__signature__ = signature

        namespace['__init__'] = __init__

    def _create_repr(namespace, signature):
        def __repr__(self):
            arguments = []
            for key, value in vars(self).items():
                arguments.append(f'{key}={value!r}')
            arguments = ', '.join(arguments)
            return f'{self.__class__.__name__}({arguments})'

        namespace['__repr__'] = __repr__

    def __new__(metaclass, name, bases, namespace):
        signature = metaclass._get_signature(namespace)
        metaclass._create_init(namespace, signature)
        metaclass._create_repr(namespace, signature)

        cls = super().__new__(metaclass, name, bases, namespace)

        return cls

