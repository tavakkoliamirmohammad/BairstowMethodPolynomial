import math


class Polynomial:
    def __init__(self, coefficient: list):
        self.coefficient = coefficient

    def __len__(self):
        return len(self.coefficient) - 1

    def __getitem__(self, item):
        return self.coefficient[len(self) - item]

    @staticmethod
    def find_quadratic_root(a: float, b: float, c: float):
        delta = b ** 2 - 4 * a * c
        roots = []
        if delta < 0:
            r1 = complex(-b / (2 * a), math.sqrt(abs(delta)) / (2 * a))
            r2 = complex(-b / (2 * a), -math.sqrt(abs(delta)) / (2 * a))
            roots.append(r1)
            roots.append(r2)
        elif delta == 0:
            r = complex(-b / (2 * a))
            roots.append(r)
        else:
            r1 = complex(-b / (2 * a) + math.sqrt(abs(delta)) / (2 * a))
            r2 = complex(-b / (2 * a) - math.sqrt(abs(delta)) / (2 * a))
            roots.append(r1)
            roots.append(r2)
        return roots

    @staticmethod
    def extended_synthetic_division(poly_dividend, poly_divisor):
        dividend = poly_dividend.coefficient
        divisor = poly_divisor.coefficient
        out = list(dividend)  # Copy the dividend
        normalizer = divisor[0]
        for i in range(len(dividend) - (len(divisor) - 1)):
            out[i] /= normalizer
            coef = out[i]
            if coef != 0:
                for j in range(1, len(divisor)):
                    out[i + j] += -divisor[j] * coef
        separator = -(len(divisor) - 1)
        return Polynomial(out[:separator])
