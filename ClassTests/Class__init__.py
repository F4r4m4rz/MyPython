class MyNoArgClass:
    def __init__(self):
        self.enabled = True
        self.name = "MyNoArgClass"

class MyArgClass:
    def __init__(self, name, enabled):
        self.enabled = True
        self.name = name

class WithMultipleOptionalArgClass:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

class WithOptionalAndMandatoryArgClass:
    def __init__(self, name, *args, **kwargs):
        self.name = name
        self.args = args
        self.kwargs = kwargs