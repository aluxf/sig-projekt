from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

As = 40
Ap = 3
Ac = 1.99
fs = 4200*6
bandpass_fs = np.array([4100,4300])
bandpass_fp = np.array([4150,4250])

lowpass_fp = 50
lowpass_fs = 100

b,a = signal.iirdesign(wp=lowpass_fp,ws=lowpass_fs,gpass=Ap,gstop=As,fs=fs,ftype="cheby2",output="ba",analog=False)
w, H = signal.freqz(b,a,fs=fs,worN=3000)

plt.plot(w,20*np.log10(np.abs(H)))
plt.grid()
plt.xlim(left=0,right=300)
#plt.axvline(x=-min_w,color="r")
#plt.axvline(x=-max_w,color="r")
#plt.axvline(x=min_w,color="r")
#plt.axvline(x=max_w,color="r")

plt.plot()

plt.show()