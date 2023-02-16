

z = 2 # global variable

def my_function(x):
    a=5
    y = x * x + z + a # y is private variable

    return y

print(my_function(x=3))

# we can use global variable inside function.
# we can't use private variable outside function.

print(z) # give output
# print(a) # give error (As it's private variable we can't use it directly outside function)


highest_grade = "A+" # Global variable

def show_class_marks():    # Not take any input
    highest_grade = "B+" # It replace the global variable (If you don't want that you can make practice to write name of variavle inside function by puting _ at last EX: highest_grade_)
    print("Highest Grade", highest_grade)
    return None # Nothing, return or return None use anything (As function is not returining anything)