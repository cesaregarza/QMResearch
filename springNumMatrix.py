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

def generateMatrix2(li):
    mat = []
    li.append('q')
    for i,x in enumerate(li):
        if i is 0:
            mat.append([x, -1 * x, *[0]*(len(li)-2)])
        elif i is (len(li) - 1):
            mat.append([*[0]*(len(li)-2),-1 * li[i - 1],li[i - 1]])
        else:
            last = li[i - 1]
            mat.append([*[0]*(i-1), -1 * last, last + x, -1 * x, *[0]*(len(li) - 2 - i)])
    return np.array(mat)

def findLambdaPrime(ar):
    ar -= k + kappa
    ar = ar ** 2
    ar -= k ** 2 + kappa ** 2
    ar /= k * kappa
    return ar 

# trivCase = np.array([firstLine, lastLine])
# eig = np.linalg.eigvals(trivCase)
# print(eig)
# print(findLambdaPrime(eig))

threeCase = generateMatrix(3)
print(threeCase)
print('threeCase')
print(np.linalg.eigvals(threeCase))

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

# sevenCase = generateMatrix(7)
# print('sevenCase')
# eig = np.linalg.eigvalsh(sevenCase.astype(np.float64))
# print(findLambdaPrime(eig))

# eightCase = generateMatrix(8)
# print('eightCase')
# print(np.linalg.eigvals(eightCase))

# tenCase = generateMatrix(10)
# print('tenCase')
# eig = np.linalg.eigvalsh(tenCase.astype(np.float64))
# print(findLambdaPrime(eig))

eightMasses = generateMatrix2([2,3,2,3,2,3,2,3])
print(eightMasses)
print(np.linalg.eigvals(eightMasses))
print(k + kappa + np.sqrt(k ** 2 + kappa ** 2 - 2 * k * kappa * np.cos(np.array([np.pi / 9, np.pi * 3 / 9, np.pi * 5 / 9, np.pi * 7/9]))))
print(k + kappa - np.sqrt(k ** 2 + kappa ** 2 - 2 * k * kappa * np.cos(np.array([np.pi / 9, np.pi * 3 / 9, np.pi * 5 / 9, np.pi * 7/9]))))