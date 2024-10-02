def count_users_with_age(data:list, job:str) -> int:
    """
    Return the number of users with a given job

    Args:
        data (dict): A dictionary of values
        job (str): The job to search for
    Returns:
        int: The number of users with the given job
    """
    
    a = 0

    for x in data:
        # if "job" in x:
        if x["job"] == job:
            a += 1
    return a

data=[
  {
    'name': 'John',
    'job': 'Barber'
  }, 
  {
    'name': 'Mary',
    'job': 'Developer'
  },
  {
    'name': 'Ann', 
    'job': 'Teacher'
  }
  ]

print(count_users_with_age(data,"Student"))