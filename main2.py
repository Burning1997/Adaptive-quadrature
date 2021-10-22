import math
import numpy as np

def f(x): return math.exp(3*x)
def g(x): return math.sin(x)+1
def w(x): return g(f(x))
def trapz( w,a,b,N):
    x = np.linspace(a,b,N+1)
    x = np.delete(x,[0,N])
    m=0
    for i in x:
       m += w(i)
    return (b - a) * (float(w(a) + w(b)) / 2 + m)/N

def recusive_trapz(w,a,b,S,tol):
    c = float(a+b)/2
    SL = trapz(w,a,c,1)
    SR = trapz(w,c,b,1)
    Sn = SL + SR
    err = abs(Sn-S)/3.0
    if err <= tol:
        S = Sn
        nodes = [a,c,b]
        return S,err,nodes
    else:
        SL,err1,nodes1 = recusive_trapz(w,a,c,SL,tol/2.0)
        SR,err2,nodes2 = recusive_trapz(w,c,b,SR,tol/2.0)
        S = SL+SR
        err = err1 + err2
        nodes = nodes1[0:-1]
        nodes.extend(nodes2)

    return SL+SR,err,nodes
def adapt_simpson(w,a,b,tol=0.005):
    S = trapz(w,a,b,1)
    S,err,nodes = recusive_trapz(w,a,b,S,tol)
    return S,err,nodes

S,err,nodes = adapt_simpson(lambda x:w(x),-1,1,0.005)
print(S,err)

