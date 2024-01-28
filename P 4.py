class PrefixMeta(type):
    def __new__(cls, name, bases, attrs):
        # Add a prefix to all attribute names
        prefixed_attrs = {f"prefixed_{key}": value for key, value in attrs.items()}
        return super().__new__(cls, name, bases, prefixed_attrs)

# Define a class with the custom metaclass
class MyClass(metaclass=PrefixMeta):
    x = 10
    y = "hello"

# Inst
