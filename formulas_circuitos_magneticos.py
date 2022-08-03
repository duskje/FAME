from sympy import symbols, diff, pprint, simplify

mu_vacio = 4 * pi 

def reluctancia(largo, area):
    mu = symbols('mu_o')
    return largo / (mu * area)


def flujo_magnetico(resistencia_equivalente):
    N = symbols('N')
    i = symbols('i')
    return (N * i) / (resistencia_equivalente)


def inductancia(resistencia_equivalente):
    """Inductancia a partir de la reluctancia equivalente"""

    N = symbols('N')
    return (N ** 2) / resistencia_equivalente


def coenergia(inductancia):
    i = symbols('i')
    return ((i ** 2) * inductancia) / 2


def fuerza_ejercida_a_partir_de_la_inductancia(inductancia):
    """Fuerza ejercida por a partir de la inductancia"""
    x = symbols('x')
    return diff(coenergia(inductancia), x)


def reluctancias_en_paralelo(R_1, R_2):
    """Reluctancia equivalente de dos reluctancias en paralelo"""

    return 1 / (1 / R_1 + 1 / R_2)


def desarrollo(expresion, tag: str):
    print(f'Expresión sin simplificar {tag}: ')
    pprint(expresion, use_unicode=False)
    print()
    print(f'Expresión simplificada {tag}: ')
    pprint(simplify(expresion), use_unicode=False)
    print()
    print()

def divisor_de_flujo(R_X, R_T):
    """Donde R_X es la reluctancia por donde queremos saber el flujo y R_T es la resistencia equivalente en paralelo a R_X"""
    phi = symbols('phi')

    return phi * (R_T / (R_X + R_T))

