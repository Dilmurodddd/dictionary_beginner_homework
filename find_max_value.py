def find_max_value(data: dict):
    """
    Return the maximum int or float value in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The maximum value in the dictionary.
    """
    lis = []

    for x in data.values():
        lis.append(x)
    lis.sort()

    return lis[-1]


data = {
    'a' : 1, 
    'b' : 2, 
    'c' : 3
  }

data  = {
    'a' : -4, 
    'b' : -10, 
    'c' : 0
  }

print(find_max_value(data))