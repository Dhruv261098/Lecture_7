
def greet_user(first_name: str, last_name: str=None): # specified the type of input we want, we get warning if we not give coorect input
    """
    A function to print first and last name
    :param first_name: the first name of the person (str)
    :param last_name: the last name of the person (str)
    :return: None
    """
    print("Hello, ", first_name, last_name)


greet_user(first_name=1, last_name=2) # incorrect parameter tyep as we mentioned str in function
greet_user("Dhruv", "Desai") # the order of the parameter matters
greet_user("Desai", "Dhruv") # the order of the parameter matters
greet_user(last_name="Desai", first_name="Dhruv") # order of the parameter does not matter