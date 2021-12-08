# args and kwargs
# def funcArgs(*args):
#     print(type(args))  # Will return tuple
#     print(args[0])


# def funcArgs(*args):
#     for item in args:
#         print(item)


# name = ["Harry", "Rohan", "Shivam", "Bedanta", "Barnil"]
# funcArgs(*name)   # * is important in both the function and the usage of it

# In a function always keep the usage in the following format `(normal, *args, **kwargs)`


def func(normal, *args, **kwargs):
    print(normal)
    for item in args:
        print(item)

    for key, value in kwargs.items():
        print(f"{key} is a {value}")


name = ["Harry", "Rohan", "Bedanta", "SkillF"]
normal = "This is normal variable"
kw = {"Harry":"Teacher", "Bedanta":"Learner", "Rohan":"Coordinator"}

func(normal, *name, **kw)
