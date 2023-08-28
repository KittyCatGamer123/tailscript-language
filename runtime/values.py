from typing import Union

ValueType = Union["number", "null"]

class RuntimeValue:
    def __init__(self, type: ValueType):
        self.type = type

class NullValue(RuntimeValue):
    def __init__(self):
        super().__init__(type="null")
        self.value = "null"

class NumberValue(RuntimeValue):
    def __init__(self, value: float):
        super().__init__(type="number")
        self.value = value
