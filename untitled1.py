# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 12:32:21 2016
 I am trying to see changes in git repository
@author: HarshaKoundinya
"""
from cvxpy import *
import tensorflow as tf

import sounddevice as sd
import numpy as np
sd.default.samplerate = 16000
from scipy.io.wavfile import read
a= read("dev1_female3_inst_mix.wav");
a1= np.array(a[1], dtype=np.int16)
sd.play(a1,blocking=True)


# Create variables and parameters.
x, y = Variable(), Variable()
a, b = Parameter(), Parameter()

# Examples of CVXPY expressions.
3.69 + b/3
x - 4*a
ty=sqrt(x) - min_elemwise(y, x - a)
print(ty)
max_elemwise(2.66 - sqrt(y), square(x + 2*y))
