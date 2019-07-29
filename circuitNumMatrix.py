import numpy as np

g = 3
k = 1
kappa = 2
w = 5

firstLine = [complex(1/w-w*(1+k),-g),w*k]
evenLine = [w*k, complex(1/w-w*(1+k+kappa),g), w*kappa]
oddLine = [w*kappa, complex(1/w-w*(1+k+kappa),-g), w*k]
lastLine = [w*k, complex(1/w-w*(1+k),g)]

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

threeCase = generateMatrix(3)
print('threeCase')
print(np.linalg.eigvals(threeCase))

fourCase = generateMatrix(4)
print('fourCase')
print(np.linalg.eigvals(fourCase))

fiveCase = generateMatrix(5)
print('fiveCase')
print(np.linalg.eigvals(fiveCase))

sixCase = generateMatrix(6)
print('sixCase')
print(np.linalg.eigvals(sixCase))

sevenCase = generateMatrix(7)
print('sevenCase')
print(np.linalg.eigvals(sevenCase))

eightCase = generateMatrix(8)
print('eightCase')
print(np.linalg.eigvals(eightCase))