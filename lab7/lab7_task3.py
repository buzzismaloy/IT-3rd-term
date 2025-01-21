'''19. Найти корень уравнения y = exp(x) – x^2 методом Брента.'''
import scipy as sp
from math import exp



def function(x: float):
    return exp(x) - x ** 2


begin: float = -2.5
end: float = 0
root = sp.optimize.brentq(function, begin, end)
print(f'{root:.6f}')
