class LengthValidator:
    def __init__(self, valid_length):
        self.valid_length = valid_length

    def __call__(self, f):
        def wrap(*arg, **args):
            x = f(*arg, **args)
            if len(x)>self.valid_length:
                raise ValueError("Maximum length exceeded")
            return x
        return wrap


@LengthValidator(5)
def set_name(name):
    return name