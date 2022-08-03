from sympy import symbols, pretty, Eq, solve, sympify
from numpy import pi

def ejercicio1_maquinas_de_corriente_continua() -> str:
    enunciado = """
Ejercicio Certamen 1

Un motor de excitación independiente tiene la armadura conectada a a una fuente de 230 V
y el campo conectado a otra fuente de 230 V. El motor gira a 1800 RPM en vacío y consume
una corriente de 5 A. La corriente de armadura nominal es de 50 A. La resistencia total del
circuito de armadura es de 0.2 Ohm. La curva de magnetización a 1800 RPM se puede aproximar
por la siguiente expresión:

e_a = -154.4442 I_f^2 + 348.4473 I_f + 58.5055 para 0.3 < I_f < 0.95

Determine la corriente de campo, torque y potencia electomagnética a corriente de armadura nominal.
"""
    desarrollo = """
Desarrollo:
n_o = 1800 RPM <- Velocidad sincrónica

Como gira en vacío:

V_a = R_a * I_a + e_a
"""

    desarrollo = []
    V_a, R_a, I_a, e_a = symbols('V_a R_a I_a e_a')
    expresion = (V_a - I_a * R_a)


    resultado_e_a = expresion.evalf(subs={V_a: 230, R_a: 0.2, I_a: 5})

    desarrollo.append(pretty(resultado_e_a, use_unicode=False) + ' = e_a')

    I_f = symbols('I_f')
    desarrollo.append(f"Luego resolviendo para I_f")

    resultado = Eq(e_a, -154.4442 * I_f ** 2 + 348.4473 * I_f + 58.5055).subs(e_a, resultado_e_a)
    resultado_I_f = str(solve(resultado, I_f))

    desarrollo.append('I_f = ' + resultado_I_f)
    desarrollo.append(f"Sólo {solve(resultado, I_f)[0]} está en el rango")

    desarrollo.append(f"Ahora, ")
    ecuacion = Eq(sympify('e_a'), sympify('K * phi * omega'))
    ecuacion = ecuacion.subs(e_a, resultado_e_a).subs('omega', 1800 * pi / 30)

    desarrollo.append(pretty(ecuacion))
    ecuacion = solve(ecuacion, 'K * phi')
    resultado_kfi = ecuacion
    desarrollo.append('K * phi = ' + pretty(ecuacion))

    ecuacion = Eq(sympify('e_a'), sympify('v_a - r_a * i_a'))
    ecuacion = ecuacion.subs('v_a', 230).subs('r_a', 0.2).subs('i_a', 50)
    resultado_e_a = solve(ecuacion, 'e_a')
    desarrollo.append('e_a = ' + pretty(resultado_e_a))

    ecuacion = Eq(sympify('e_a'), sympify('k * phi * omega'))
    ecuacion = ecuacion.subs('k * phi', resultado_kfi).subs('e_a', resultado_e_a)
    resultado_omega = solve(ecuacion, 'omega')
    desarrollo.append(pretty(resultado_omega) + ' = omega')
    desarrollo.append(str(resultado_e_a[0] / resultado_kfi[0]) + ' = omega')
    i_a_nominal = 50
    v_a_nominal = 220
    desarrollo.append('T_e = ' + str(resultado_kfi[0] * i_a_nominal))
    desarrollo.append('P_e = ' + str(v_a_nominal * i_a_nominal))

    desarrollo = '\n\n'.join(desarrollo)
    return enunciado + desarrollo


def ejercicio2_maquinas_de_corriente_continua() -> str:
    enunciado = """
Ejercicio Certamen 2
Una máquina de corriente continua de 75 kW, 400 V, 220 A, 1000 RPM, tiene una resistencia de armadura de 0.1 Ohm.
La tensión de campo es de 240 V. La constante de la máquina es 66 y el flujo por polo nominal es de 54.8 mWb.
La armadura se alimenta desde un conversor dual trifásico sin corriente circulante alimentado desde una red de 380 V.
El campo se alimenta desde un conversor híbrido monofásico alimentado de 380 V.
  
a) Determine el ángulo de disparo del conversor de armadura y de campo para condiciones nominales. (Suponga que no
hay corte de corriente)
b) Determine el ángulo de disparo y el conversor AC/DC activo (converter 1 o 2) bajo las siguientes condiciones de operación 
(suponga que no hay corte de corriente)

I) Velocidad 500 RPM y T_e = 300 Nm
II) Velocidad 500 RPM y T_e = -300 Nm
III) Velocidad -500 RPM y T_e = 300 Nm
IV) Velocidad -500 RPM y T_e = -300 Nm
"""

    desarrollo = []

    desarrollo.append('Parte a)')
    desarrollo.append('Para obtener el ángulo de disparo para el campo:')

    ecuacion1 = Eq(
        sympify('V_campo'),
        sympify('V_fuente * (sqrt(2) / pi) * (1 + cos(alpha))')
    )

    desarrollo.append(pretty(ecuacion1) + ' (Ecuacion1)')

    ecuacion1 = ecuacion1.subs('V_campo', 240).subs('V_fuente', 380)
    desarrollo.append(pretty(ecuacion1) + ' (sustituyendo los valores)')

    resolviendo_para_alfa = solve(ecuacion1, 'alpha')
    desarrollo.append(pretty(resolviendo_para_alfa[1]) + ' (resolviendo para alfa)')

    desarrollo.append('alpha = ' + pretty(resolviendo_para_alfa[1].evalf()) + ' rad (evaluando)')

    desarrollo.append('Para obtener el ángulo de disparo para la armadura:')
    desarrollo.append('Esta es la expresión para obtener el voltaje de armadura')

    ecuacion2 = Eq(
        sympify('V_a'),
        sympify('V_fuente * (3 * sqrt(2) / pi) * cos(alpha)')
    )

    desarrollo.append(pretty(ecuacion2) + ' (ecuacion2)')
    ecuacion2 = (ecuacion2
                 .subs('V_a', 400)
                 .subs('V_fuente', 380))

    desarrollo.append(pretty(ecuacion2) + ' (sustituyendo los valores)')

    resolviendo_para_alfa = solve(ecuacion2, 'alpha')
    desarrollo.append(pretty(resolviendo_para_alfa[1]) + ' (resolviendo para alfa)')
    desarrollo.append('alpha = ' + pretty(resolviendo_para_alfa[1].evalf()) + ' rad (evaluando)')

    desarrollo.append("""
Parte b)
Subparte I

Primero se obtiene a I_a y a e_a, para luego 
obtener el voltaje necesario y de ahí finalmente obtener el ángulo de disparo""")
    ecuacion3 = Eq(sympify('e_a'), sympify('K * phi * omega'))
    desarrollo.append(pretty(ecuacion3) + ' (ecuacion 3)')
    ecuacion3 = ecuacion3.subs('K', 66).subs('phi', 0.0547).subs('omega', 500 * pi / 30)
    desarrollo.append(pretty(ecuacion3.evalf()) + ' (evaluando)')

    ecuacion4 = Eq(sympify('i_a'), sympify('T_e / (K * phi)'))
    desarrollo.append(pretty(ecuacion4) + ' (ecuacion 4)')
    ecuacion4 = ecuacion4.subs('K', 66).subs('phi', 0.0547).subs('T_e', 300)
    desarrollo.append(pretty(ecuacion4.evalf()) + ' (evaluando)')

    ecuacion5 = Eq(sympify('v_a'), sympify('e_a + r_a * i_a'))
    desarrollo.append(pretty(ecuacion5) + ' (ecuacion 5)')

    ecuacion5 = Eq(sympify('v_a'), sympify('e_a + r_a * i_a'))
    ecuacion5 = ecuacion5.subs('e_a', ecuacion3.rhs).subs('r_a', 0.1).subs('i_a', ecuacion4.rhs)
    desarrollo.append(pretty(ecuacion5.evalf()) + ' (evaluando)')

    ecuacion6 = Eq(
        sympify('V_a'),
        sympify('V_fuente * (3 * sqrt(2) / pi) * cos(alpha)')
    )

    desarrollo.append(pretty(ecuacion6) + ' (ecuacion 6)')
    ecuacion6 = (ecuacion6
                 .subs('V_a', ecuacion5.rhs)
                 .subs('V_fuente', 380))

    desarrollo.append(pretty(ecuacion6) + ' (sustituyendo los valores)')

    resolviendo_para_alfa = solve(ecuacion6, 'alpha')
    desarrollo.append(pretty(resolviendo_para_alfa) + ' (resolviendo para alfa)')
    desarrollo.append('alpha = ' + pretty(min(resolviendo_para_alfa).evalf()) + ' rad (evaluando)')

    desarrollo.append("""
Como i_a > 0, es el primer converter. 
Subparte II
""")

    ecuacion3 = Eq(sympify('e_a'), sympify('K * phi * omega'))
    desarrollo.append(pretty(ecuacion3) + ' (ecuacion 3)')
    ecuacion3 = ecuacion3.subs('K', 66).subs('phi', 0.0547).subs('omega', 500 * pi / 30)
    desarrollo.append(pretty(ecuacion3.evalf()) + ', ahora n = 500 (evaluando)')

    ecuacion4 = Eq(sympify('i_a'), sympify('T_e / (K * phi)'))
    desarrollo.append(pretty(ecuacion4) + ' (ecuacion 4)')
    ecuacion4 = ecuacion4.subs('K', 66).subs('phi', 0.0547).subs('T_e', -300)
    desarrollo.append(pretty(ecuacion4.evalf()) + ', Ahora T_e = -300 (evaluando)')

    ecuacion5 = Eq(sympify('v_a'), sympify('e_a + r_a * i_a'))
    desarrollo.append(pretty(ecuacion5) + ' (ecuacion 5)')

    ecuacion5 = Eq(sympify('v_a'), sympify('e_a + r_a * i_a'))
    ecuacion5 = ecuacion5.subs('e_a', ecuacion3.rhs).subs('r_a', 0.1).subs('i_a', ecuacion4.rhs)
    desarrollo.append(pretty(ecuacion5.evalf()) + ' (evaluando)')

    ecuacion6 = Eq(
        sympify('V_a'),
        sympify('V_fuente * (3 * sqrt(2) / pi) * cos(alpha)')
    )

    desarrollo.append(pretty(ecuacion6) + ' (ecuacion 6)')
    ecuacion6 = (ecuacion6
                 .subs('V_a', ecuacion5.rhs)
                 .subs('V_fuente', 380))

    desarrollo.append(pretty(ecuacion6) + ' (sustituyendo los valores)')

    resolviendo_para_alfa = solve(ecuacion6, 'alpha')
    desarrollo.append(pretty(resolviendo_para_alfa) + ' (resolviendo para alfa)')
    desarrollo.append('alpha = ' + pretty(min(resolviendo_para_alfa).evalf()) + ' rad (evaluando)')
    desarrollo.append('alpha = ' + pretty(min(resolviendo_para_alfa) * 180/pi) + ' deg (evaluando)')

    desarrollo.append(f"""
Como i_a < 0, es el segundo converter. En donde el ángulo de disparo es: {pretty(180 - min(resolviendo_para_alfa) * 180/pi)} deg
Subparte III
""")

    desarrollo = '\n\n'.join(desarrollo)

    return enunciado + desarrollo

def ejercicio1_maquinas_de_induccion():
    enunciado = """
Ejercicio Certamen 1

Un motor de inducción trifásico de cuatro polos, conectaedo en Y de 460 V (línea a línea), 25 kW y 60hz
tiene los siguientes parámetros de circuito equivalente en ohm por fase referidos al estator:

R_1=0.103 || R_2=0.0225 || X_1=1.10 || X_2=1.13 || X_m = 59.4

Las pérdidas totales por fricción y rozamiento con el aire se consideran constantes a 265 W y las pérdidas
en el núcleo pueden considerarse igual a 220 W. Con el motor conectado directamente a una fuente de 460 V,
calcule para un deslizamiento de 3%:

a) Velocidad de rotación, Torque y potencia mecánica electromagnética.
b) Torque y potencia en el eje.
c) Rendimiento y factor de potencia.
d) Corriente y torque de partida.
e) Torque máximo y la velocidad para torque máximo.
"""

def maquinas_de_corriente_continua():
    pass


def maquinas_de_induccion():
    pass

maquinas_de_corriente_continua.__doc__ = (
        ejercicio1_maquinas_de_corriente_continua()
#        + ejercicio2_maquinas_de_corriente_continua()
)

help(maquinas_de_corriente_continua)