class MyException(Exception):
    def __init__(self, msg = 'Incorrect data'):
        super().__init__(msg)

class MyTypeError(MyException):
    def __init__(self, msg = 'Incorrect data type'):
        super().__init__(msg)

class MyValueError(MyException):
    def __init__(self, msg = 'Incorrect value for operation'):
        super().__init__(msg)
