import scipy.integrate as integrate
from numpy import pi
from sympy import symbols

from formulas_circuitos_magneticos import (
    reluctancia,
    inductancia,
    coenergia,
    reluctancias_en_paralelo,
    desarrollo,
    fuerza_ejercida_a_partir_de_la_inductancia,
)

# x, A_1, A_2, mu, d= symbols('x A_1 A_2 mu d')

# R_1 = reluctancia(x, A_1, mu)
# R_2 = reluctancia(d - x, A_2, mu)
# R_T = R_1 + R_2
#
# desarrollo(R_1, 'R_1')
# desarrollo(R_2, 'R_2')
# desarrollo(R_T, 'R_T')
#
# N, i = symbols('N i')
#
# phi = flujo_magnetico(N, i, R_T)
# desarrollo(phi, 'phi')

def ejercicio1certamen():
    d, x, l, g, h = symbols('d x l g h')

    R_1 = reluctancia(2*g + h, l * x)
    R_2 = reluctancia(2*g, l * (d - x))

    desarrollo(R_1, 'R_1')
    desarrollo(R_2, 'R_2')

    R_eq = reluctancias_en_paralelo(R_1, R_2)
    desarrollo(R_eq, 'R_eq')

    L = inductancia(R_eq)
    desarrollo(L, 'L')

    W = coenergia(L)
    desarrollo(W, 'W')

    f = fuerza_ejercida_a_partir_de_la_inductancia(L)

    desarrollo(f, 'f')

    f2 = f.evalf(subs={'N': 5.0})

    desarrollo(f2, 'f2')


if __name__ == '__main__':
    ejercicio1certamen()