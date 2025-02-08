"""
Avoid conflicts with already existing names -> Python “remembers” two things: the variable’s identifier, and the value that is passed to it.
Functions, classes, objects, modules, packages… they’re all namespaces.
"""

# Use the namespaces to make your code clearer and more readable
from datetime import datetime  # instead of from datetime.datetime import now

print(datetime.now())
