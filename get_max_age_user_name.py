def get_max_age_user_name(data:list) -> str:
    """
    Return the name of the user with the maximum age in a dictionary.

    Args:
        data (dict): A dictionary of values
    Returns:
        str: The name of the user with the maximum age in the dictionary
    """

    """ insonlarning yoshi 0 dan kichhgina bo'lmaganligi 
    sababli a o'zgaruvchini 0 ga tengladim
    
    a = data[0]["age"] 
    
    """

    a = 0
    b = data[0]["name"]

    for x in data:
        if x["age"] > a:
            a = x["age"]
            b = x["name"]

    return b


data = [
  {
    'name': 'John', 
    'age': 27
  }, 
  {
    'name': 'Mary', 
    'age': 42
  }
]


data = [
  {
    'name': 'John', 
    'age': 32
  }, 
  {
    'name': 'Mary', 
    'age': 18
  }, 
  {
    'name': 'Ann', 
    'age': 20
  }, 
  {
    'name': 'Ban', 
    'age': 29
  }
]



print(get_max_age_user_name(data))