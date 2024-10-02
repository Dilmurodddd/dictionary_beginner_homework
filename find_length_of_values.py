def find_length_of_values(data: dict) -> int:
    """
    Return the sum of the length of all values in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The sum of the length of all values in the dictionary.
    """
    da = 0

    for k,v in data.items():
        da += len(data[k])

    return da

data1 = {
    'a': 'abc',
    'b': 'def', 
    'c': 'ghi'
  }

data2 = find_length_of_values(data1)

print(data2)