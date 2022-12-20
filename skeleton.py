#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Skeleton for the wireless communication system project in Signals and
Transforms

For plain text inputs, run:
$ python3 skeleton.py "Hello World!"

For binary inputs, run:
$ python3 skeleton.py -b 010010000110100100100001

2020-present -- Roland Hostettler <roland.hostettler@angstrom.uu.se>
"""

import sys
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import wcslib as wcs

def main():
    # Parameters
    # TODO: Add your parameters here. You might need to add other parameters as 
    # well.
    channel_id = 16   # Your channel ID
    Tb = 0.06           # Symbol width in seconds
    fc = 4200
    wc = 2*np.pi*fc
    fs = 6*fc          # Sampling frequency in Hz
    As = 40
    Ap = 3
    Ac = 1.99

    bp_fs = [4100,4300]
    bp_fp = [4150,4250]

    lp_fp = 50
    lp_fs = 100

    'Bandpass filter'
    bp_b,bp_a = signal.iirdesign(wp=bp_fp,ws=bp_fs,gpass=Ap,gstop=As,fs=fs,ftype="cheby2",output="ba",analog=False)

    'Lowpass filter'
    lp_b,lp_a = signal.iirdesign(wp=lp_fp,ws=lp_fs,gpass=Ap,gstop=As,fs=fs,ftype="cheby2",output="ba",analog=False)
    # Detect input or set defaults
    string_data = True
    if len(sys.argv) == 2:
        data = str(sys.argv[1])

    elif len(sys.argv) == 3 and str(sys.argv[1]) == '-b':
        string_data = False
        data = str(sys.argv[2])

    else:
        print('Warning: No input arguments, using defaults.', file=sys.stderr)
        data = "Hello World!"

    # Convert string to bit sequence or string bit sequence to numeric bit
    # sequence
    if string_data:
        bs = wcs.encode_string(data)
    else:
        bs = np.array([bit for bit in map(int, data)])

    # Encode baseband signal
    xb = wcs.encode_baseband_signal(bs, Tb, fs)

    # TODO: Put your transmitter code here (feel free to modify any other parts
    # too, of course)
    '''
    1. Baseband signal encoding,
    2. modulation, and
    3. band-limitation.
    '''
    
    'Modulation'
    'bs kan vara fel här'
    xm = xb*Ac*np.sin(wc*bs) 

    'Band-limitation'
    xt = signal.lfilter(b=bp_b,a=bp_a,x=xm)

    # Channel simulation
    # TODO: Enable channel simulation.
    yr = wcs.simulate_channel(xt, fs, channel_id)

    
    # TODO: Put your receiver code here. Replace the three lines below, they
    # are only there for illustration and as an MWE. Feel free to modify any
    # other parts of the code as you see fit, of course.
    yb = xb*np.exp(1j*np.pi/5) + 0.1*np.random.randn(xb.shape[0])
    ybm = np.abs(yb)
    ybp = np.angle(yb)

    # Baseband and string decoding
    br = wcs.decode_baseband_signal(ybm, ybp, Tb, fs)
    data_rx = wcs.decode_string(br)
    print('Received: ' + data_rx)


if __name__ == "__main__":
    main()
