
class Shipping:

    _next_serial = 1337

    @staticmethod
    def _get_next_serial():
        result = Shipping._next_serial
        Shipping._next_serial += 1
        return result

    def __init__(self, code, content):
        self._code = code
        self._content = content
        self._serial = Shipping._get_next_serial()