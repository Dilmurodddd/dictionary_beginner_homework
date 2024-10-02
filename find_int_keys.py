def find_int_keys(data: dict) -> list:
    """
    Return a list of all keys in a dictionary that are integers.
    Args:
        data (dict): A dictionary of values
    Returns:
        list: A list of all keys in the dictionary that are integers.
    """
    a = []

    for x in data:
        for k in x.keys():
            if type(k) == int:
                a.append(x[k])
    
    return a

data = [
  {
    'name': 'John',
    'job': 'Barber',
    1:"a"
  }, 
  {
    'name': 'Mary',
    'job': 'Developer'
  },
  {
    'name': 'Ann', 
    'job': 'Teacher',
    6:"d"
  },
  ]

print(find_int_keys(data))