# required arguments & optional arguments
# required always define first than optional



# first_name is a required parameter
# last_name is an optional parameter
def greet_user(first_name, last_name=None): # here for last name default value is none so when you not specify any value for this parameter it will take none as default
    print("Hello, ", first_name, last_name)

# You can specify as many inputs you want by separating by ','

greet_user(first_name="Dhruv")
greet_user(first_name="Dhruv", last_name="Desai")





