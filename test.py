import numpy as np
import matplotlib.pyplot as plt

M = 253

def get_Tb(wc):
    return M*2*np.pi / wc
'''
def Xb(w,N,wc):
    Tb = get_Tb(wc)
    sum_ = 0
    for n in range(0,N):
        sum_ += np.sinc(w*Tb / (2 * np.pi)) * np.e**(-1j*w*(n+1/2))
    return Tb * sum_
'''

def Xb(w,Ac,N,wc):
    Tb = get_Tb(wc)
    return Tb * np.array(
        [np.sum(np.abs([1/2 * 1j *Ac * np.sinc(omega*Tb / (2 * np.pi)) * np.e**(-1j*omega*(n+1/2)) for n in range(0,N)])) 
        for omega in w]
    )

def Xm(w,Ac,N, wc):
    return (Xb(w=(w + wc),Ac=Ac,N=N,wc=wc) - Xb(w=(w - wc),Ac=Ac,N=N,wc=wc))

min_freq = 4150
max_freq = 4250
w_min = 2*np.pi*min_freq
w_max = 2*np.pi*max_freq
wc = 2*np.pi*4200
wvec = np.arange(w_min,w_max,0.1)
Xm_mag = np.abs(Xm(w=wvec,Ac=1.99,N=1,wc=wc))

fig,ax = plt.subplots()
ax.set_xlim(xmin=4150,xmax=4250)
ax.grid()
ax.plot(wvec / (2*np.pi),Xm_mag)
#plt.axvline(x=-min_w,color="r")
#plt.axvline(x=-max_w,color="r")
#plt.axvline(x=min_w,color="r")
#plt.axvline(x=max_w,color="r")

plt.plot()

plt.show()