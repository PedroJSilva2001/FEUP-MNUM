#Ex 1
from math import sin, cos, exp
def f(x,y): return sin(x+y)-exp(x-y)

def g(x,y): return cos(x+y)-(x**2)*(y**2)

def fderx(x,y): return cos(y+x)-exp(x-y)

def fdery(x,y): return cos(y+x)+exp(x-y)

def gderx(x,y): return -sin(y+x)-(2*x)*y**2

def gdery(x,y): return -sin(y+x)-(2*x**2)*y

def J(x,y): return fderx(x,y)*gdery(x,y)-gderx(x,y)*fdery(x,y)

def h(x,y): return -(f(x,y)*gdery(x,y)-g(x,y)*fdery(x,y))/J(x,y)
def k(x,y): return -(fderx(x,y)*g(x,y)-gderx(x,y)*f(x,y))/J(x,y)

def newton(x0, y0, n):
    for i in range(n):
        x0copy = x0
        x0 = x0 + h(x0, y0)
        y0 = y0 + k(x0copy, y0)
        print(x0, y0) 

newton(0.5, 0.25, 2)
print()

#Ex 2
#a) matriz diagonalmente dominante - I
#b) eliminacao gauss - III (pivot já a um) 
#c)
def g1(x_next,y,z): return (1.2-103*x_next-41*z)/61 
def g2(x,y,z): return (0-5.5*y-3*z)/1
def g3(x_next,y_next,z): return (-13-2*x_next-10*y_next)/13

def gauss_seidel(x0,y0,z0, n):
    for i in range(n):
        x0 = g1(x0, y0, z0)
        y0 = g2(x0, y0, z0)
        z0 = g3(x0, y0, z0)
        print(x0, y0, z0)
print()


#Ex 3 
hx = (2.0-0)/2.0
hy = (2.0-0)/2.0
def simpson(x0, x1, x2, y0, y1, y2, f00, f01, f02, f10, f11, f12, f20, f21, f22):
    return (hx*hy)/9.0*(f00 +f02 + f20 + f22 + 4*(f10 + f12 + f01 + f21) + 16*f11)

print(simpson(0, 1,2, 0, 1, 2, 1.1, 1.4, 9.8, 2.1, 4, 2.2, 7.8, 1.5, 1.2))
print()

#Ex 4

#dy/dx = z
#dz/dx = -By + Az
h = 0.20000
x0 = 0.40000
A = -7
B = 4
def a(x,y,z): return z
def b(x,y,z): return -B*y+A*z

def euler(x0,y0,z0, n, f, g):
    for i in range(n):
        y0_copy = y0
        y0 = y0 + h*f(x0, y0, z0)
        z0 = z0 + h*g(x0, y0_copy, z0)
        x0 = x0 + h
        print(x0, y0, z0)
euler(x0, 2.0, 1.0, 3, a, b)

print()
#Ex 5

#É possível descubrir de duas maneiras distintas: ou usa-se um método direto de procura de minimos ou obtém-se a derivada da função
#e vê-se as suas raízes com algum algoritmo de procura se raízes.

# Nos métodos diretos é preciso começar com um intervalo [x1, x2] onde sabemos que existe só um minimo porque a função mantém a mesma
# concavidade nele. Para isto é preciso ver o gráfico da função y. Pode-se usar a pesquisa simples em que dá-se um passo em x numa
# direção onde a função diminui e para-se quando num dado passo a função aumenta, que é uma solução brute-force e não permite enquadrar
# bem o intervalo novo onde está o minimo. Pode-se usar o método dos terços que envolve dividir o intervalo em 3 mas que quando um dos
# intervalos é excluido, não é usado nas iterações seguintes. A regra áurea trata isto ao aproveitar o mais baixo valor calculado.

# Procurar o minimo através da procura da raiz da derivada poderia ser trabalhoso ja que é preciso a derivada mas este nao é o caso
# porque a função é um simples polinómio e visto que já é preciso um intervalo onde está o mínimo, ter um intervalo para a raiz não
# é problema. Pode-se aplicar portanto a bissecção que chega ao valor exato do minimo. Melhor ainda é usar o método de Newton visto 
# que como a derivada é muito vertical perto da raiz, o algoritmo converge muito mais depressa também para o valor exato, ao contrário
# dos metodos diretos que só dão um intervalo onde poderá estar.

#Aplicou-se então o método de Newton com o guess x0 = 3 e em 10 iterações obteve-se que o minimo é x = 1.0, batendo certo com 
# a solução analítica    

def y(x): return (x-3)**2+x**4
def yder(x): return 2*(x-3)+4*x**3
def yderder(x): return 2+12*x**2

def newton2(x0, f,fder, n):
    for i in range(n):
        x0 = x0-f(x0)/fder(x0)
    print(x0)
newton2(3, yder, yderder, 10)

def bissection(a,b,f, n):
    for i in range(n):
        c = (a+b)/2.0
        if f(c)*f(a) < 0:
            b = c
        elif f(c)*f(a) > 0:
            a = c
    print(c)
bissection(0,3,yder, 50)

def aurea(x1, x2, y, n):
    B = (5**0.5 -1)/2.0
    A = B**2
    x3 = x1 + A*(x2 - x1)
    x4 = x1 + B*(x2-x1)
    for i in range(n):
        if y(x3) < y(x4):
            x2 = x4
            x4 = x3
            x3 = x1 + A*(x2-x1)
        else:
            x1 = x3
            x3 = x4
            x4 = x1 + B*(x2-x1)
        print([x1,x2,x3,x4])
aurea(0,2, y, 100)

print()

#Ex 6

#a = 0.4523 * 10^4
#b = 0.2115 * 10^-3
#c = 0.2583 * 10*1
#b = 0.00000002115 * 10^4 = 0  
#c = 0.0002583 * 10^4 = 0.0002 * 10^4
#c+b+a = (0.0002 + 0 + 0.4523) *10^4 = 0.4525 E+4
#erro absoluto = 4525.5832115 - 4525 = 0.5832 E+0
#erro relativo = (4525.5832115 - 4525)/4525.5832115 * 100= 0.013% 
