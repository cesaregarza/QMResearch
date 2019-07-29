import matplotlib.pyplot as plt
import numpy as np

# x axis
u = np.arange(0.0,2.74,0.01,dtype=np.cdouble)
v = np.arange(2.74,5.0,0.01,dtype=np.cdouble)
x = np.arange(0.0,5.0,0.01,dtype=np.cdouble)
y = np.arange(0.0,3.83,0.01, dtype=np.cdouble)
z = np.arange(3.83,5.0,0.01, dtype=np.cdouble)
 
# y axis
def f(t, option = 0):
    c = 1
    b = np.sqrt(t ** 4 - 16 * t ** 2 + 20)
    a = -t ** 2 +8
    if option % 2 == 1:
        b *= -1
    if option > 1:
        c = -1
    return c * np.sqrt(a+b)/np.sqrt(complex(22))

def g(t, option = 0):
    c = 1
    b = np.sqrt(t ** 4 - 8 * t ** 2 + 4)
    a = 4 - t ** 2
    if option % 2 == 1:
        b *= -1
    if option > 1:
        c = -1
    return c * np.sqrt(a+b)/np.sqrt(complex(6))
    
 
# use LaTeX fonts in the plot
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

n = plt.figure()

# plot
plt.subplot(2,1,1)
for i in range(4):
    plt.plot(x, np.real(f(x,i)), color="black")
    plt.plot(x, np.real(g(x,i)), color="black")

plt.axvline(x=0.733, color = "black", alpha = 0.5, dashes = (2,2))
plt.axvline(x=3.83, color = "black", alpha = 0.5, dashes = (2,2))
# set labels (LaTeX can be used)
plt.title(r'\textbf{Symmetry Breaking}', fontsize=11)
plt.ylabel(r'\textbf{Re[$\omega$]}', fontsize=11)

plt.subplot(2,1,2)
for i in range(4):
    plt.plot(y, np.imag(f(y,i)), color="black")
    plt.plot(z, np.imag(f(z,i)), color="black")
    plt.plot(u, np.imag(g(u,i)), color="black")
    plt.plot(v, np.imag(g(v,i)), color="black")
# set labels (LaTeX can be used)
plt.axvline(x=0.733, color = "black", alpha = 0.5, dashes = (2,2))
plt.axvline(x=3.83, color = "black", alpha = 0.5, dashes = (2,2))
plt.xlabel(r'\textbf{$\gamma$}', fontsize=11)
plt.ylabel(r'\textbf{Im[$\omega$]}', fontsize=11)

plt.show()

# save as PDF
n.savefig("pt_breaking.pdf",)
