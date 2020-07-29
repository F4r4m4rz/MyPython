class CallCount:
    def __init__(self, f):
        self.counter =0
        self.f = f

    def __call__(self, *args, **kwargs):
        self.counter +=1
        self.f(*args, **kwargs)


@CallCount
def say_hello(name):
    print("Hello {}".format(name))