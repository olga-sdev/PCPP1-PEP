"""
Blank lines, called vertical whitespaces: supports readability and code division.
"""

# two blank lines to surround top-level function and class definitions
class ClassExample:
    pass


def function_example():
    pass
  

# single blank line to surround method definitions inside a class
class ClassExample:
    def function_1(self):
        pass

    def function_2(self):
        pass


# blank lines in functions in order to indicate logical sections
def function_example():
    variable_example = 'variable'
    
    if isinstance(variable_example, str):
        return 'variable is a str type'
    else:
        return 'variable is an other type then str'
