class NoArgClass:
    def __call__(self):
        print("Call is called")


class WithMandatoryArg:
    def __call__(self, name):
        print("Call is called with {}".format(name))