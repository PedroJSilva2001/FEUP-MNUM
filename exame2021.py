import math
# EX 1
# Dado que se apresenta uma equação diferencial de 1ª ordem, pode-se recorrer a um de 4 métodos númericos para o resolver:
# o método de euler, primeira ordem, euler modificado, 3 ordem, runge kutta 2, segunda ordem e runge kutta 4, quarta ordem, 
# todos eles são baseados em integração no sentido de usarem conhecimento da derivada de x(t) que é f(x,t) para estimar 
# a função. A ordem do método diz o número de estimativas ou médias ponderadas que faz para obter o próximo ponto
# Aumentando a ordem dos métodos, a solução, teóricamente, fica mais exata e o erro diminui cada vez mais se o passo
# diminuir para metade. O runge kutta 4 poderá ser usado dado que usa 4 estimas para aproximar o gráfico, ou seja, é o que
# usa mais informação para obter os pontos. Visto que este método fornece um conjunto de pontos e não a expressão analítica 
# da função, seria preciso fazer uma espécie de regressão com os pontos obtidos no rk4 que poderá ser feito por exemplo com os
# minimos quadrados, que pondera muito mais os grandes desvios que os pequenos nos valores. Pode-se também ver que tipo de padrão seguem
# os pontos e escolher a regressão apropriada (linear, quadrática, exponencial, logaritmica...). Obtendo-se uma expressão pode-se aplicar
# um método para descubrir raízes reais, que poderá ser feito com 5 métodos: método da bissecção, corda ou falsa posição, corda modificado, 
# Newton e Picard-Peano. A bissecção e os dois da corda convergem sempre portanto não haveria os perigos do picard peano ou newton, que têm
# condições de convergência. Para os dois da corda e para a bissecção seria só preciso fornecer um intervalo [a,b] em que só exista uma e uma só
# raíz e tal que f(a) e f(b) tenham sinais diferentes. A Corda converge na maioria dos casos mais depressa que a bissecção porque a sua aproximação
# usa os valores f(a), f(b), a e b (c = a*f(b) - b*f(a)/f(b)-f(a)) ao contrário da bissecção, que usa só a e b (c = a+b/2). Se fosse usado o picard peano, 
# seria preciso pôr x(t) = 0 na forma t = g(t) e verificar que |g'(t)| < 1 na região da suposta raíz e fornecer um t0 inicial. Se fosse usado o Newton, teria-se logo
# a derivada de x porque dx/dt = f(x,t). Contudo, o método tem muitos perigos como a função x e a derivada x' não serem contínuas, ocorrer divisão por zero
# num ponto estacionário, ocorrer oscilação do método (nunca convergir) entre os mesmos valores quando a raíz é por exemplo num ponto de inflexão e divergir completamente
# se o guess for afastado. Portanto, recomenda-se o método da corda/corda modificado dado que converge sempre e não exige conhecimento da derivada. 


# EX 2
F = [0.0, 0.30, 0.60, 0.90, 1.20, 1.50, 1.80, 2.1, 2.4]
alpha = [0.0, 0.07, 0.13, 0.20, 0.26, 0.33, 0.40, 0.46, 0.53]


def trap(F, alpha, h):
    area = 0
    for i in range(0, len(F), h):
        if i == 0 or i == len(F)-1:
            area += F[i]*math.cos(alpha[i])
        else :
            area += 2*F[i]*math.cos(alpha[i])
    return area * 2.0*  math.pi * h/2.0 

#Resolveu-se com a regra dos trapézios com h = 4, h' = 2, h'' = 1
# seja S o resultado com h, S' com h' e S'' com h'':
s = trap(F, alpha, 4)
s1 = trap(F, alpha, 2)
s2 = trap(F, alpha, 1)
qc = (s1-s)/(s2-s1)
e = (s2-s1)/3.0
print("s =", s)
print("s' =", s1)
print("s'' =", s2)
print("Qc =", qc)
#que nao é exatamente aproximado a 4 (2^ordem do método) logo não
#se pode estimar o erro. Calcula-se na mesma mas é de menção que teóricamente
#só se pode estimar se o quociente de convergência for aproximadamente 4
print("e'' =", e, "\n")


# EX 3
def g1(x,y,z,t):
    return (2.5 - 0.5*y - 3*z - 0.25*t)/6

def g2(x,y,z,t):
    return (3.8 - 1.2*x - 0.25*z - 0.20*t)/3

def g3(x,y,z,t):
    return (10  + 1*x - 0.25*y - 2*t)/4

def g4(x,y,z,t):
    return (7 - 2*x - 4*y - 1*z)/8

def gauss_seidel(g1,g2,g3,g4, n, x0, y0, z0, t0):
    for i in range(n):
        x0 = g1(x0, y0, z0, t0)
        y0 = g2(x0, y0, z0, t0)
        z0 = g3(x0, y0, z0, t0)
        t0 = g4(x0, y0, z0, t0)
    print(x0, y0, z0, t0, "\n")

gauss_seidel(g1, g2, g3, g4,1, -0.81959, 1.40167, 2.15095, 0.11019)

# EX 4
# x**3 +2x**2 + 10*x - 46 só tem uma raíz entre [-0.4, 3.6]

# EX 5
def f(x):
    return x**3 + 2*x**2 + 10*x - 46 

def fder(x):
    return 3*x**2 + 4*x + 10 

def newton(f,fder, n, x0):
    print(x0)
    for i in range(n):
        x0 = x0 - f(x0)/fder(x0)
        print(x0)
    print()
newton(f, fder, 2, 0)

