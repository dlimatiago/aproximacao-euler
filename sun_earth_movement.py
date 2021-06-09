import numpy as np
from tqdm import trange as progress
from animate import Animar


def mod(coor: np.array):
    return (np.sum(coor ** 2)) ** 0.5


def aprox_euler():
    for tempo in progress(tempos - 1):
        Fg = mu * (r[tempo] / mod(r[tempo]) ** 3)

        v[tempo + 1] = v[tempo] - Fg * dt
        r[tempo + 1] = r[tempo] + v[tempo] * dt


def passo(n=365):
    print(f'Trajetoria da Terra em {n} dias\n')

    for _ in range(n):
        print(f'Dia {_ + 1}, no instante t = {t[_]:.5} dia')

        print(f'Posição radial da Terra: {mod(r[_] * km_Gm): .3e} Gm')
        print(f'Módulo da velocidade da Terra:  {mod(v[_]): .3e} Gm/dia')

        F = mu * Mt * (r[_] / mod(r[_]) ** 3)
        print(f'Módulo Força Gravitacional sobre a Terra: {mod(F): .3e} KgGm/dia²')

        print('\n', '-' * 100, '\n')


print('Simulador de órbita em relação ao Sol')
# ----------------------------------------------------------------------------------------------------------------------
G = 6.673 * 1e-11  # Constante de Gravitação Universal em m³/kgs²
Ms = 1.9885 * 1e30  # Massa do Sol em kg
Mt = 5.9722 * 1e24  # Massa da Terra em kg

# ----------------------------------------------------------------------------------------------------------------------
# Conversão de unidade
m_Gm = 1e-9 ** 3  # Conversão de metros ao cubo para gigametros ao cubo
s_dia = (1 / 60 / 60 / 24) ** 2  # segundo quadrado para dia quadrado
fator = m_Gm / s_dia  # Fator de correção de m³/s² para Gm³/dia²
mu = G * Ms * fator  # Mu em Gm³/ kg dia²

km_Gm = 1e-3  # Conversão de kilômetros para gigametros
ms2_Gmdia = 3600 * 24 * 1e-9  # Conversão de m/s² para Gm/dia²
# ----------------------------------------------------------------------------------------------------------------------
# Condições de análise
tf = int(input('Tempo em dias para analisar: '))  # Tempo total a ser analisado em dias
dt = 10 / 24 / 60 / 60  # Passo temporal a ser dado dentro do período total
tempos = int(tf / dt)  # Número que multiplicado pelo passo temporal, resulta no tempo total para se analisar

# ----------------------------------------------------------------------------------------------------------------------
# Definição dos vetores
t = np.arange(tempos) * dt  # vetor com os instantes de tempo
r = np.zeros((tempos, 2))  # Vetor posição da Terra em n instantes de tempo
v = np.zeros((tempos, 2))  # Vetor velocidade da Terra em n instates de tempo

# ----------------------------------------------------------------------------------------------------------------------
# Condições iniciais
xi, yi = map(float, input('Vetor posição inicial (x, y) em mil km: ').split(','))
vx, vy = map(float, input('Vetor velocidade inicial (x, y) em m/s²: ').split(','))

r[0] = [xi, yi]  # Vetor posição inicial da Terra

v[0] = [vx * ms2_Gmdia, vy * ms2_Gmdia]  # Vetor velocidade inicial da Terra
# r[0,0] -> tempo zero na componente 0 (x)

# Cálculo da aproximação numérica
aprox_euler()
Animar(r).animation()
