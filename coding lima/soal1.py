import numpy as np
import matplotlib.pyplot as plt

t0 = 0
tn = 450
ndata = 2500

t = np.linspace(t0,tn,ndata)
h = t[2]-t[1]

N = 2500
I0 = 25
R0 = 3
S0 = N - I0 - R0

I = np.zeros(ndata)
R = np.zeros(ndata)
S = np.zeros(ndata)

I[0] = I0
R[0] = R0
S[0] = S0

beta = 0.5
gamma = 0.2

for n in range(0,ndata-1):
  S[n+1] = S[n] - h*beta/N*S[n]*I[n]
  I[n+1] = I[n] + h*beta/N*S[n]*I[n] - h*gamma*I[n]
  R[n+1] = R[n] + h*gamma*I[n]

plt.plot(t,S,label='S')
plt.plot(t,I,label='I')
plt.plot(t,R,label='R')
plt.legend()
plt.show()
