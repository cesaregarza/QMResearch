from sympy import *
init_printing(use_unicode = True)

# w = Symbol('w')
# k = Symbol('k')
# kappa = Symbol("k'")
# g = Symbol('g')

w, k, kappa, g = symbols("w k k' g")


a, b, c, d = symbols('a b c d')
firstLine = [-I*g+1/w-w*(1+k),w*k]
evenLine = [w*k, I*g+1/w-w*(1+k+kappa), w*kappa]
oddLine = [w*kappa, -I*g+1/w-w*(1+k+kappa), w*k]
lastLine = [w*k, I*g+1/w-w*(1+k)]



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

# trivialCase = Matrix([firstLine, lastLine])
# trivDet = trivialCase.det()
# trivP, trivD = trivialCase.diagonalize()
# pprint(trivD)

twoCase = Matrix([[*firstLine, 0, 0], [*evenLine, 0], [0, *oddLine], [0, 0, *lastLine]])
# twoDet = twoCase.det()
# twoP, twoD = twoCase.diagonalize()
# pprint(twoD)
pprint(simplify(twoCase.eigenvals()))

threeCase = generateMatrix(3)
# # threeDet = threeCase.det()
# # threeP, threeD = threeCase.diagonalize()
threeEigen = threeCase.eigenvals()
pprint(solve(threeEigen, w))
pprint(simplify(threeEigen))

fourCase = generateMatrix(4)
fourEigen = fourCase.eigenvals()
pprint(simplify(fourEigen))

# fiveCase = generateMatrix(5)
# fiveEigen = fiveCase.eigenvals()
# pprint(simplify(fiveEigen))

# sixCase = generateMatrix(3)
# pprint(sixCase)
# sixEigen = sixCase.eigenvals()
# pprint(sixEigen)