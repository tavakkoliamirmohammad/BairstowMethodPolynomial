from Polynomial import Polynomial
from RootFinder import RootFinder

n = input()
coeff = list(map(int, input().split()))
poly = Polynomial(coeff)
root_finder = RootFinder(10 ** -6, poly, -2.1, -1.9)
roots = root_finder.find()

real_sum = 0
imag_sum = 0

for root in roots:
    if root.imag >= 0:
        real_sum += root.real
        imag_sum += root.imag
print("%.6f" % real_sum + " %.6f" % imag_sum)
