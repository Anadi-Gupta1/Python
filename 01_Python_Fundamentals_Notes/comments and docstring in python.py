# what is comments and docstring in python
# Comments are used to explain code and make it more readable. They are ignored by the Python interpreter.
# Docstrings are a type of comment used to describe the purpose of a function, class, or module. They are enclosed in triple quotes and can span multiple lines.
# Comments start with a hash symbol (#) and continue to the end of the line.
# Docstrings are written as the first statement in a function, class, or module and can be accessed using the `__doc__` attribute.
# Example of a single-line comment
# This is a single-line comment
# Example of a multi-line comment
"""
This is a multi-line comment.
It can span multiple lines.
"""
# Example of a docstring
def example_function():
    """
    This is a docstring for the example_function.
    It describes what the function does.
    """
    pass  # This function does nothing
# Example of a class with a docstring
class ExampleClass:
    """
    This is a docstring for the ExampleClass.
    It describes what the class represents.
    """
    def __init__(self):
        pass  # This constructor does nothing
# Example of a module docstring
