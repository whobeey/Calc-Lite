from time import time
from math import *

_factorial = factorial
_sin = sin
_cos = cos
_tan = tan
_asin = asin
_acos = acos
_atan = atan
_log = log
_abs = abs

class _Logic:
    @staticmethod
    def record(func):
        def timer(*args):
            print(f"Started running method: {func.__name__}()")
            start = time()

            result = func(*args)

            end = time()
            print(f"Stopped running method: {func.__name__}(), Time: {(end - start):.6f}")
            return result
        return timer

    @staticmethod
    def verify(func):
        def process(self, *args):
            try:
                args = tuple(float(a) for a in args)
            except TypeError or ValueError:
                return error["not_supported"]

            return func(self, *args)
        return process

    @record
    @verify
    def add(self, x, y):
        return x + y

    @record
    @verify
    def minus(self, x, y):
        return x - y

    @record
    @verify
    def multiply(self, x, y):
        return x * y

    @record
    @verify
    def divide(self, x, y):
        try:
            return x / y
        except ZeroDivisionError:
            return error["is_zero"]

    @record
    @verify
    def abs(self, x):
        return _abs(x)

    @record
    @verify
    def factorial(self, x):
        if x < 0:
            return error["is_negative"]
        if x % 1 != 0:
            return error["not_whole"]
        return _factorial(int(x))
    
    @record
    @verify
    def square(self, x):
        return x ** 2
    
    @record
    @verify
    def power(self, x, y):
        return x ** y
    
    @record
    @verify
    def square_root(self, x):
        if x < 0:
            return error["is_negative"]
        return x ** (1 / 2)
    
    @record
    @verify
    def root(self, x, y):
        if x or y == 0:
            return error["is_zero"]
        elif y % 2 != 0:
            return error["not_supported"]
        return x ** (1 / y)
    
    @record
    @verify
    def convert(self, x, _type):
        match _type.lower().strip():
            case "radian":
                return x * (pi / 180)
            case "degree":
                return x * (180 / pi)
            case _:
                return error["not_supported"]
    

    @record
    @verify
    def sin(self, x):
        return _sin(x)

    @record
    @verify
    def cos(self, x):
        return _cos(x)

    @record
    @verify
    def tan(self, x):
        return _tan(x)
    
    @record
    @verify
    def csc(self, x):
        if _sin(x) == 0:
            return error["is_zero"]
        
        return 1 / _sin(x)

    @record
    @verify
    def sec(self, x):
        if _cos(x) == 0:
            return error["is_zero"]
        
        return 1 / _cos(x)

    @record
    @verify
    def cot(self, x):
        if _tan(x) == 0:
            return error["is_zero"]
        
        return 1 / _tan(x)
    
    @record
    @verify
    def arcsin(self, x):
        if x < -1 or x > 1:
            return error["not_range"]
        return _asin(x)

    @record
    @verify
    def arccos(self, x):
        if x < -1 or x > 1:
            return error["not_range"]
        return _acos(x)

    @record
    @verify
    def arctan(self, x):
        return _atan(x)
    
    @record
    @verify
    def arccsc(self, x):
        if abs(x) < 1:
            return error["not_range"]
        return _asin(1 / x)

    @record
    @verify
    def arcsec(self, x):
        if abs(x) < 1:
            return error["not_range"]
        return _acos(1 / x)

    @record
    @verify
    def arccot(self, x):
        if x == 0:
            return error["is_zero"]

        return _atan(1 / x)
    
    @record
    @verify
    def log(self, x, base):
        if x < 0:
            return error["is_negative"]
        elif x == 0:
            return error["is_zero"]
        
        match base.lower().strip():
            case 10:
                return log10(x)
            case 'e':
                return _log(x)
            case _:
                return _log(x, base)

error = {"not_supported" : "Error: Invalid Value Input.",
         "not_whole" : "Error: Not a Whole Number.",
         "not_range" : "Please enter a valid value between -1 and 1",
         "is_zero" : "Error: Cannot Input Zero",
         "is_negative" : "Error: Negative Input",
         "is_complex" : "Error: Complex Numbers Unsupported"}

calc = _Logic()