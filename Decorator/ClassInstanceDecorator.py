class MyDecorator:
    def __init__(self, name):
        self.name = name

    def __call__(self, f):
        def wrap(*args, **kwargs):
            x = f(*args, **kwargs)
            print("Decoreted by {}".format(self.name))
            return x
        return wrap


@MyDecorator("First decorator")
def my_printer(message):
    print("Message is {}".format(message))


@MyDecorator("Second decorator")
def my_sqrt(n):
    return n **2