def get_user_names_with_age_range(data:list, min_age:int, max_age:int) -> list:
    """
    Return a list of users with a given age range

    Args:
        data (dict): A dictionary of values
        min_age (int): The minimum age to search for
        max_age (int): The maximum age to search for
    Returns:
        list: A list of users with the given age range
    """
    min_l = []
    max_l = []

    for x in data:
        if x["age"] > min_age:
            min_l.append(x)
        if x["age"] < max_age:
            max_l.append(x)

    minn = min_l[0]["age"]
    min_name = min_l[0]["name"]
    
    maxx = max_l[0]["age"]
    max_name = max_l[0]["name"]

    for x in min_l:
        if x["age"] > minn:
            minn = x["age"]
            min_name = x["name"]
    for x in max_l:
        if x["age"] > maxx:
            maxx = x["age"]
            max_name = x["name"]
    return min_name,max_name


data = [
  {
    'name': 'John', 
    'age': 20
  }, 
  {
    'name': 'Mary', 
    'age': 17
  },
  {
    'name': 'Ban', 
    'age': 23
  },
  {
    'name': 'John', 
    'age': 27
  }
]

data = [
  {
    'name': 'Anny', 
    'age': 20
  }, 
  {
    'name': 'Mary', 
    'age': 30
  }
]


print(get_user_names_with_age_range(data,18,25))