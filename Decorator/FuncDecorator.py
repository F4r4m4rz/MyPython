def my_decorator(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        print("Calling {}".format(f))
        return x

    return wrap


@my_decorator
def rotate_list(my_list):
    return my_list[1:] + [my_list[0]]