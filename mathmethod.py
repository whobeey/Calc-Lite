#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 26 23:30:37 2026

@author: xuzikang
"""

class mathmethods:
    def add(self,a,b):
        return a+b

    def minus(self,a,b):
        return a-b

    def multiply(self,a,b):
        return a*b

    def divide(self,a,b):
        return a/b

    def sine(self,a,b=10):
        result = 0
        sign = 1
        denominator = 1
        numerator = a
        for i in range(b):
            result += numerator*sign / denominator
            sign *= -1
            numerator *= a * a
            denominator *= (2*i + 2) * (2*i + 3)
        return result

    def cosine(a, b=10):
        result = 0.0
        sign = 1.0
        numerator = 1.0
        denominator = 1
        for i in range(b):
            result += sign * numerator / denominator
            sign *= -1
            numerator *= a * a
            denominator *= (2 * i + 1) * (2 * i + 2)
        return result

    def tangent(a, b=10):
        result = 0
        sign = 1
        for i in range(1, 2 * b, 2):
            result += sign * (a ** i)
            sign *= -1
        return result

    def arcsin(a, b=10):
        if a < -1 or a > 1:
            return "Undefined"

        result = 0.0

        for n in range(b):
            # calculate (2n)!
            fact_2n = 1
            for i in range(1, 2 * n + 1):
                fact_2n *= i

            # calculate n!
            fact_n = 1
            for i in range(1, n + 1):
                fact_n *= i

            numerator = fact_2n * (a ** (2 * n + 1))
            denominator = (4 ** n) * (fact_n ** 2) * (2 * n + 1)

            result += numerator / denominator

        return result

    def arccos(a, b=10):
        if a < -1 or a > 1:
            return "Undefined"

        PI = 3.14

        # calculate arcsin(x)
        arcsin_x = 0.0

        for n in range(b):
            # calculate (2n)!
            fact_2n = 1
            for i in range(1, 2 * n + 1):
                fact_2n *= i

            # calculate n!
            fact_n = 1
            for i in range(1, n + 1):
                fact_n *= i

            numerator = fact_2n * (a ** (2 * n + 1))
            denominator = (4 ** n) * (fact_n ** 2) * (2 * n + 1)

            arcsin_x += numerator / denominator

        # arccos(x) = π/2 − arcsin(x)
        return PI / 2 - arcsin_x

    def arctan(a, b):
        PI = 3.141592653589793
        result = 0.0
        sign = 1

        if a > 1:
            a = 1 / a
            offset = PI / 2
        elif a < -1:
            a = 1 / a
            offset = -PI / 2
        else:
            offset = 0

        for i in range(b):
            result += sign * (a ** (2 * i + 1)) / (2 * i + 1)
            sign *= -1

        return offset + result

    def square(a):
        return a * a

    def square_root(a):
        if a < 0:
            return "Undefined"

        x = a
        for _ in range(10):  #iterations
            x = (x + a / x) / 2

        return x
