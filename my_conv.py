import numpy as np
def  myconv(h,x):

############################################################################
# A function to generate the output signal y as convolution of input signal
# x and impulse response signal h
############################################################################

# INPUT PARAMETERS---------------------------------------------------------
# x: input signal
# h: impulse response
    len_x = len(x) # length of x
    len_h = len(h) # length of h
############################################################################
# Data processing: convolution (TO BE COMPLETED BY STUDENTS)
############################################################################
# OUTPUT PARAMETERS--------------------------------------------------------
# y: output signal as convolution of input signal x and impulse response h

# Write the code including comments to explain what you are doing
    y = np.zeros(len_x)
    for n in range(len_x):
        y[n] = sum(x[m]*h[n-m] for m in range(max(0, n-len_h+1), min(len_x-1, n)))
    print(len_x)
    print(len_h)
    return y
