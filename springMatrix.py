from sympy import *
init_printing(use_unicode = True)

# w = Symbol('w')
# k = Symbol('k')
# kappa = Symbol("k'")
# g = Symbol('g')

w, k, kappa, g = symbols("w k k' g")
# k = 2
# kappa = 3


a, b, c, d = symbols('a b c d')
firstLine = [k, -k]
evenLine = [-k, k + kappa, -kappa]
oddLine = [-kappa, k+kappa, -k]
lastLine = [-k, k]

firstLine1 = [a, -a]
evenLine1 = [-a, a+b, -b]
oddLine1 = [-b, b+c, -c]
evenLine2 = [-c, b+c, -b]
oddLine2 = [-b, b+a, -a]
lastLine1 = [-c, c]



def generateMatrix(size):
    mat = []
    mat.append([*firstLine, *[0]*2*(size-1)])
    for i in range((size - 1) * 2):
        if i % 2 is 0:
            mat.append([*[0]*i, *evenLine, *[0]*(2*(size-1)-i - 1)])
        else:
            mat.append([*[0]*i, *oddLine, *[0]*(2*(size - 1) - i - 1)])
    mat.append([*[0]*2*(size - 1), *lastLine])
    return Matrix(mat)

def generateMatrix2(size):
    mat = []
    twoSize = 4 * size - 2
    mat.append([*firstLine1, *[0]*twoSize])
    for i in range(2 * size - 1):
        if i % 2 is 0:
            mat.append([*[0]*(2*i), *evenLine1, *[0]*(twoSize-(2 * i + 1))])
            mat.append([*[0]*(2*i + 1), *oddLine1, *[0]*(twoSize - (2 * i + 2))])
        else:
            mat.append([*[0]*(2*i), *evenLine2, *[0]*(twoSize - (2 * i + 1))])
            mat.append([*[0]*(2*i + 1), *oddLine2, *[0]*(twoSize - (2 * i + 2))])
    mat.append([*[0]*(twoSize), *lastLine1])

    return Matrix(mat)

def findLambdaPrime(di):
    li = []
    for key, value in di.items():
        eq = Eq(key, k + kappa + sqrt(k ** 2 + a * k * kappa + kappa ** 2))
        li.append(solve(eq,a))
    
    return li


# trivialCase = Matrix([firstLine, lastLine])
# trivDet = trivialCase.det()
# trivP, trivD = trivialCase.diagonalize()
# pprint(trivD)

# twoCase = Matrix([[*firstLine, 0, 0], [*evenLine, 0], [0, *oddLine], [0, 0, *lastLine]])
# # twoDet = twoCase.det()
# # twoP, twoD = twoCase.diagonalize()
# # pprint(twoD)
# pprint(twoCase)
# pprint(simplify(twoCase.eigenvals()))
# pprint(simplify(twoCase.eigenvects()))


# threeCase = generateMatrix(3)
# threeDet = threeCase.det()
# threeP, threeD = threeCase.diagonalize()
# pprint(threeCase)
# threeEigen = threeCase.eigenvals()
# pprint(simplify(threeEigen))
# pprint(findLambdaPrime(threeEigen))
# pprint(simplify(threeCase.eigenvects()))

twoCase = generateMatrix2(1)
pprint(twoCase)
pprint(simplify(twoCase.eigenvals()))
