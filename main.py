
import math


def f(x): return math.exp(3*x)
def g(x): return math.sin(x)+1
def w(x): return g(f(x))


def simpson(w, a, b, N):
    if N % 2 == 0:
       n = N
    else:
       n = N+1

    h = float(b-a)/n
    S = float(w(a))

    for i in range(1, n, 2):
        x = a + h * i
        S += 4*w(x)

    for i in range(2, n-1, 2):
        x = a+h*i
        S += 2*w(x)

    S += w(b)
    S = h * S/3

    return S
def recusive_simpson(w, a, b, S, tol):
    c = float(a+b)/2
    SL = simpson(w, a, c, 1)
    SR = simpson(w, c, b, 1)
    Sn = SL + SR
    err = abs(Sn-S)/15.0
    if err <= tol:
        S = Sn
        nodes = [a, c, b]
        return S, err, nodes
    else:
        SL, err1, nodes1 = recusive_simpson(w, a, c ,SL, tol/2.0)
        SR, err2, nodes2 = recusive_simpson(w, c, b, SR, tol/2.0)
        S = SL+SR
        err = err1 + err2
        nodes = nodes1[0:-1]
        nodes.extend(nodes2)

    return SL+SR, err, nodes
def adapt_simpson(w, a, b, tol=0.005):
    S = simpson(w, a, b, 1)
    S, err, nodes = recusive_simpson(w, a, b, S, tol)
    return S, err, nodes

S, err, nodes = adapt_simpson(lambda x:w(x), -1, 1, 0.005)
print(S, err)


