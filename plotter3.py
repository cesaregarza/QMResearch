import matplotlib.pyplot as plt
import numpy as np

# x axis
x = np.arange(0.0,40.0,1,dtype=np.cdouble)
kc = 3.59
kk = 8.75
mm = 0.507
m = 20


firstLine = [kc, -kc]
evenLine = [-kc, kc + kk, -kk]
oddLine = [-kk, kc + kk, -kc]
lastLine = [-kc, kc]

firstLine1 = [kc + kk, -kc]
lastLine1 = [-kc, kc + kk]

def generateMatrix(size, typee = 0):
    mat = []

    if typee is 0:
        fLine = firstLine
        lLine = lastLine
    else:
        fLine = firstLine1
        lLine = lastLine1

    mat.append([*fLine, *[0]*2*(size-1)])
    for i in range((size - 1) * 2):
        if i % 2 is 0:
            mat.append([*[0]*i, *evenLine, *[0]*(2*(size-1)-i - 1)])
        else:
            mat.append([*[0]*i, *oddLine, *[0]*(2*(size - 1) - i - 1)])
    mat.append([*[0]*2*(size - 1), *lLine])
    return np.array(mat)
 
# y axis
def f(t, theta):
    l = (theta * np.pi) / m
    return kc + kk + np.sqrt(kc ** 2 + kk ** 2 - 2 * kc * kk * np.cos(l))

def g(t, theta):
    l = (theta * np.pi) / m
    return kc + kk - np.sqrt(kc ** 2 + kk ** 2 - 2 * kc * kk * np.cos(l))

def fm(t, theta):
    l = (theta * np.pi) / m
    return - 1 * (kc + kk + np.sqrt(kc ** 2 + kk ** 2 - 2 * kc * kk * np.cos(l)))

def gm(t, theta):
    l = (theta * np.pi) / m
    return - 1 * (kc + kk - np.sqrt(kc ** 2 + kk ** 2 - 2 * kc * kk * np.cos(l)))

    
 

# use LaTeX fonts in the plot
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

n = plt.figure()

# plot
# for i in range(m):
#     if i < 2:
#         continue
#     x = np.arange(1.0, i, 1.0)
#     for j in range(i):
#         plt.plot(i, f(i, j), 'ro')
#         plt.plot(i, g(i, j), 'ro')
#         plt.plot(i, fm(i, j), 'ro')
#         plt.plot(i, gm(i, j), 'ro')

tenCase = generateMatrix(10,1)
eig = np.linalg.eigvalsh(tenCase.astype(np.float64))

elevenCase = generateMatrix(11)
eig2 = np.linalg.eigvalsh(elevenCase.astype(np.float64))
# print(eig2)

mat = []
lnth = len(eig2)
j = 0
prev = 0
for x in np.nditer(eig2):
    if j is 0:
        prev = x
        j += 1
        continue
    else:
        mat.append((prev + x)/2)
        prev = x
        j += 1

print(mat)
print(eig)


# plt.plot(x, eig, 'bo')

# for i in range(1, m+1):
    
#     plt.plot(i+19, f(i, i-1), 'r^')
#     plt.plot(i, g(i, m-i), 'r^')

# # plt.plot(x, f(x,0), color="black")
# # plt.plot(x, f(x, m-1), color = "black")
# # plt.fill_between(x, f(x,0), f(x, m-1), color="black", alpha = 0.3)

# # plt.plot(x, gm(x, 1), color = "black")
# # plt.plot(x, g(x, 1), color = "black")
# # plt.fill_between(x, gm(x, 1), g(x, 1), color = "black", alpha = 0.3)

# # plt.plot(x, fm(x,0), color="black")
# # plt.plot(x, fm(x, m-1), color = "black")
# # plt.fill_between(x, fm(x,0), fm(x, m-1), color="black", alpha = 0.3)


# # plt.axvline(x=0, color = "black", alpha = 0.5, dashes = (2,2))
# # plt.axvline(x=1, color = "black", alpha = 0.3, dashes = (2,2))

# # plt.axhline(y=0, color="black", alpha=0.5, dashes=(2,2))
# # plt.axhline(y=np.sqrt(kc * 2), color="black", alpha=0.5, dashes=(2,2))
# # plt.text(2.15, np.sqrt(kc * 2)-0.4, r'\textbf{$ \sqrt{2 k_c}$}', color="black")
# # plt.axhline(y=- np.sqrt(kc * 2), color="black", alpha=0.5, dashes=(2,2))
# # plt.text(2.15, -np.sqrt(kc * 2)-0.4, r'\textbf{$-\sqrt{2 k_c}$}', color="black")

# # set labels (LaTeX can be used)
# plt.title(r'\textbf{Normal Mode Band Splitting}', fontsize=11)
# plt.ylabel(r'\textbf{Normal Mode $( \omega )$}', fontsize=11)
# plt.xlabel(r'\textbf{$n$}', fontsize = 11)

# plt.show()

# # save as PDF
# # n.savefig("bandSplitting.pdf",)
