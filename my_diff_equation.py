
import numpy as np
def my_diffequation(x, alpha, N):

############################################################################
# A function to generate the output signal y of the system described by a
# diffence equation
############################################################################

# INPUT PARAMETERS---------------------------------------------------------
# x: input signal
# alpha: decreasing amplitude
# N: delay between consecutive echoes

############################################################################
# Data processing (TO BE COMPLETED BY STUDENTS)
############################################################################
# OUTPUT PARAMETERS--------------------------------------------------------
# y: output signal

    L=len(x)
    print(L)
    # Write the code including comments to explain what you are doing
    y = np.zeros(L)

    for i in range(L):
        print(i)
        if (i < N):
            y[i] = x[i]
            print(y[i])
        else:
            y[i] = x[i] - alpha*y[i-N] 
       
    #y = [(x[i] + alpha*x[i-N]) for i in range(x)]

    return y
