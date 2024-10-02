def find_max_key(data: dict):
    """
    Return the maximum int or float key in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The maximum key in the dictionary.
    """
    lis = []

    for x in data.keys():
        lis.append(x)
    
    lis.sort()
    return lis[-1]


data = {
    1: 'a', 
    2: 'b', 
    3: 'c'
  }

data = {
    1.4 :'a', 
    7.8 :'b', 
    4 : 'c'
  }

print(find_max_key(data))