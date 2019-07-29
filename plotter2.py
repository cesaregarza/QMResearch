import matplotlib.pyplot as plt
import numpy as np

# x axis
x = np.arange(0.0,2.0,0.001,dtype=np.cdouble)
kc = 10
m = 500

 
# y axis
def f(t, theta):
    kk = kc * t
    l = (theta * np.pi) / m
    return np.sqrt(kc + kk + np.sqrt(kc ** 2 + kk ** 2 - 2 * kc * kk * np.cos(l)))

def g(t, theta):
    kk = kc * t
    l = (theta * np.pi) / m
    return np.sqrt(kc + kk - np.sqrt(kc ** 2 + kk ** 2 - 2 * kc * kk * np.cos(l)))

def fm(t, theta):
    kk = kc * t
    l = (theta * np.pi) / m
    return - 1 * np.sqrt(kc + kk + np.sqrt(kc ** 2 + kk ** 2 - 2 * kc * kk * np.cos(l)))

def gm(t, theta):
    kk = kc * t
    l = (theta * np.pi) / m
    return - 1 * np.sqrt(kc + kk - np.sqrt(kc ** 2 + kk ** 2 - 2 * kc * kk * np.cos(l)))

    
 

# use LaTeX fonts in the plot
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

n = plt.figure()

# plot
plt.plot(x, f(x,0), color="black")
plt.plot(x, f(x, m-1), color = "black")
plt.fill_between(x, f(x,0), f(x, m-1), color="black", alpha = 0.3)

plt.plot(x, gm(x, 1), color = "black")
plt.plot(x, g(x, 1), color = "black")
plt.fill_between(x, gm(x, 1), g(x, 1), color = "black", alpha = 0.3)

plt.plot(x, fm(x,0), color="black")
plt.plot(x, fm(x, m-1), color = "black")
plt.fill_between(x, fm(x,0), fm(x, m-1), color="black", alpha = 0.3)


plt.axvline(x=0, color = "black", alpha = 0.5, dashes = (2,2))
plt.axvline(x=1, color = "black", alpha = 0.3, dashes = (2,2))

plt.axhline(y=0, color="black", alpha=0.5, dashes=(2,2))
plt.axhline(y=np.sqrt(kc * 2), color="black", alpha=0.5, dashes=(2,2))
plt.text(2.15, np.sqrt(kc * 2)-0.4, r'\textbf{$ \sqrt{2 k_c}$}', color="black")
plt.axhline(y=- np.sqrt(kc * 2), color="black", alpha=0.5, dashes=(2,2))
plt.text(2.15, -np.sqrt(kc * 2)-0.4, r'\textbf{$-\sqrt{2 k_c}$}', color="black")

# set labels (LaTeX can be used)
plt.title(r'\textbf{Normal Mode Band Splitting}', fontsize=11)
plt.ylabel(r'\textbf{Normal Mode $( \omega )$}', fontsize=11)
plt.xlabel(r'\textbf{$k_k = x \cdot k_c$}', fontsize = 11)

plt.show()

# save as PDF
n.savefig("bandSplitting.pdf",)
