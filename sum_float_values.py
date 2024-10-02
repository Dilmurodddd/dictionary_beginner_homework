def sum_float_values(data: dict) -> float:
    '''
    Return the sum of all float values in dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        float: The sum of all float values in the dictionary.
    '''
    a = 0
    for x in data.values():
        if type(x) == float:
            a += x
    return a

data = {
    'a': 1, 
    'b' : 2.5, 
    'c': 3.0
  }

print(sum_float_values(data))