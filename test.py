class MyCustomException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"MyCustomException: {self.message}"


def some_function(value):
    if value < 0:
        raise MyCustomException("Value cannot be negative")


try:
    some_function(-1)
except MyCustomException as e:
    print(e)
