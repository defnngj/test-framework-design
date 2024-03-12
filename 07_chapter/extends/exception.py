# exception.py

class CustomException(Exception):
    """
    自定义异常类
    """

    def __init__(self, msg: str = None):
        self.msg = msg

    def __str__(self):
        exception_msg = f"Message: {self.msg}\n"
        return exception_msg


class AgeError(CustomException):
    """
    Age error
    """
    pass


class HeightError(CustomException):
    """
    Height error
    """
    pass


class WeightError(CustomException):
    """
    Weight error
    """
    pass
