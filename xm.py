import sys
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import wcslib as wcs

channel_id = 16   # Your channel ID
Tb = 0.06           # Symbol width in seconds
fc = 4200
wc = 2*np.pi*fc # 26389
fs = 24*fc          # Sampling frequency in Hz, 25200
As = 40
Ap = 3
Ac = 1.99
data = "Hello World!"

bp_fs = [4100,4300]
bp_fp = [4150,4250]
lp_fp = 50
lp_fs = 100
'Bandpass filter'
bp_b,bp_a = signal.iirdesign(wp=bp_fp,ws=bp_fs,gpass=Ap,gstop=As,fs=fs,ftype="cheby2",output="ba",analog=False)


bs = wcs.encode_string(data)
xb = wcs.encode_baseband_signal(bs, Tb, fs)


'1512 samples = 0.06s'

x_vec = np.arange(0, len(xb))
xc = Ac*np.sin(wc/fs*x_vec)
xm = xb*xc
xt = signal.lfilter(b=bp_b,a=bp_a,x=xm)
#plt.plot(x_vec, xc)
fig,ax = plt.subplots()


#ax.plot(x_vec, xb)
#ax.plot(x_vec, xc)
#ax.plot(x_vec, xm)
ax.plot(x_vec, xt)
ax.grid()
ax.set_xlim(left=0, right=10100)

#plt.axvline(x=-min_w,color="r")
#plt.axvline(x=-max_w,color="r")
#plt.axvline(x=min_w,color="r")
#plt.axvline(x=max_w,color="r")

plt.plot()

plt.show()