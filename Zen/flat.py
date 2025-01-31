"""
Flat code -> for better management.

Nesting code (above 3 levels) ->  makes it difficult to understand.
"""


def get_temperature(temperature):
    return ['Cold' if -89 < temperature < 10 else 'Warm']


print(get_temperature(13))
