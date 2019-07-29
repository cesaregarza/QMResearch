import numpy as np
# import scipy as sp

k = 2
kappa = 3

firstLine = [k, -k]
evenLine = [-k, k + kappa, -kappa]
oddLine = [-kappa, k + kappa, -k]
lastLine = [-k, k]

def generateMatrix(size):
    mat = []
    mat.append([*firstLine, *[0]*2*(size-1)])
    for i in range((size - 1) * 2):
        if i % 2 is 0:
            mat.append([*[0]*i, *evenLine, *[0]*(2*(size-1)-i - 1)])
        else:
            mat.append([*[0]*i, *oddLine, *[0]*(2*(size - 1) - i - 1)])
    mat.append([*[0]*2*(size - 1), *lastLine])
    return np.array(mat)

def findLambdaPrime(ar):
    ar -= k + kappa
    ar = ar ** 2
    ar -= k ** 2 + kappa ** 2
    ar /= k * kappa
    return ar  

trivCase = np.array([firstLine, lastLine])
eig = np.linalg.eigvals(trivCase)
print(eig)
print(findLambdaPrime(eig))

# threeCase = generateMatrix(3)
# print('threeCase')
# print(np.linalg.eigvals(threeCase))

# fourCase = generateMatrix(4)
# print('fourCase')
# print(np.linalg.eigvals(fourCase))

# fiveCase = generateMatrix(5)
# print('fiveCase')
# print(np.linalg.eigvals(fiveCase))

# sixCase = generateMatrix(6)
# print('sixCase')
# eig = np.linalg.eigvals(sixCase)
# print(findLambdaPrime(eig))

sevenCase = generateMatrix(7)
print('sevenCase')
eig = np.linalg.eigvalsh(sevenCase.astype(np.float64))
print(findLambdaPrime(eig))

# eightCase = generateMatrix(8)
# print('eightCase')
# print(np.linalg.eigvals(eightCase))

tenCase = generateMatrix(10)
print('tenCase')
eig = np.linalg.eigvalsh(tenCase.astype(np.float64))
print(findLambdaPrime(eig))