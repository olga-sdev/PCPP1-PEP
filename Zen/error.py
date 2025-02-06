"""
Better: program that crashes to debug.
Worse: program that silences an error.
Raising an exception -> data about the reason of error.
"""

set_for_calculation = (20, 'str', True)

for data in set_for_calculation:
    print(type(data))
    try:
        calculate = [data + 2 for data in set_for_calculation]
    except TypeError as type_err:
        print(f'Error occurred with value "{data}" in a list {set_for_calculation}: {type_err}')
