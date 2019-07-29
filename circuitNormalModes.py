from sympy import *
init_printing(use_unicode = True)

w = Symbol('w')
k = Symbol('k')
kappa = Symbol("k'")
g = Symbol('g')
a, b, c, d = symbols('a b c d')

trivialCase = [-w * (1+k) + sqrt(-g ** 2+k ** 2*w ** 2)+1/w, -w*(1+k) - sqrt(-g ** 2+k ** 2*w ** 2)+1/w]

def solver(li):
    output = set()
    for i in li:
        x = solve(i, w)
        output.update(x)
    
    return(output)

def pprinter(li,subs=False):
    for i in li:
        if subs is False:
            pprint(simplify(i))
        else:
            pprint(simplify(i.subs(subs)))

def generateEigenValues(li):
    mat = [*trivialCase]
    base = -w * (1+k+kappa) + 1/w
    for i in li:
        mat.append(base + sqrt(-(g ** 2) + (w ** 2) * (k ** 2 + i * k * kappa + kappa ** 2) ))
        mat.append(base - sqrt(-(g ** 2) + (w ** 2) * (k ** 2 + i * k * kappa + kappa ** 2) ))
    
    return mat


        

twoCase = [0]
twoEig = generateEigenValues(twoCase)
pprinter(solver(twoEig),{k: 1, kappa: 2})
