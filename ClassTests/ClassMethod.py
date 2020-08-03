import pprint


class AbstractShipping:

    _code = None
    _tracking_code = None
    _tracking_number_seq = 0

    def _get_next_tracking_seq(cls):
        result = cls._tracking_number_seq
        cls._tracking_number_seq += 1
        return result

    def _method_templates(self):
        self._generate_tracking_code()
        self._print_shipping_info()

    def print_items(self):
        return self._print_shipping_info()

    def generate_tracking_code(self):
        return self._generate_tracking_code()


class Shipping(AbstractShipping):

    _tracking_number_seq = 1234

    @property
    def code(self):
        return self._code

    def __init__(self, code, items):
        self._code = code
        self._items = items
        self._tracking_number = Shipping._get_next_tracking_seq(type(self))

    def _print_shipping_info(self):
        pprint.pprint(self._items)

    def _generate_tracking_code(self):
        self._tracking_code = "EN {}".format(self._tracking_number) \
            if self._tracking_code is None else self._tracking_code
        return self._tracking_code

    @classmethod
    def shipping_creator(cls, code, item):
        return cls(code, item)


class RefrigaratorShipping(Shipping):

    _tracking_number_seq = 24

    @property
    def code(self):
        return self._code
    
    @code.setter
    def code(self, value):
        pass
    
    @code.deleter
    def code(self):
        pass

    def __init__(self, code, items, temperature):
        super().__init__(items, code)
        self._temperature = temperature

    def _print_shipping_info(self):
        super()._print_shipping_info()
        print("Maximum temperature is {}".format(self._temperature))

    def _generate_tracking_code(self):
        self._tracking_code = "PTESE {}".format(self._tracking_number) \
            if self._tracking_code is None else self._tracking_code
        return self._tracking_code

    @classmethod
    def shipping_creator(cls, code, items, temperature):
        return cls(code, items, temperature)