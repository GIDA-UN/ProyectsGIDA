import numpy as np
from scipy.signal import butter, lfilter, freqz
import matplotlib.pyplot as plt


def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y


# Filter requirements.
order = 6
fs = 1000      # sample rate, Hz

cutoff = 15  # desired cutoff frequency of the filter, Hz
index=10
textFile='P'+str(index)+'/P'+str(index)+'.txt'
textSave='P'+str(index)+'/result.txt'

# Get the filter coefficients so we can check its frequency response.
b, a = butter_lowpass(cutoff, fs, order)

# Plot the frequency response.
w, h = freqz(b, a, worN=8000)
plt.subplot(2, 1, 1)
plt.plot(0.5*fs*w/np.pi, np.abs(h), 'b')
plt.plot(cutoff, 0.5*np.sqrt(2), 'ko')
plt.axvline(cutoff, color='k')
plt.xlim(0, 0.5*fs)
plt.title("Lowpass Filter Frequency Response (cutoff="+str(cutoff)+")")
plt.xlabel('Frequency [Hz]')
plt.grid()


# Demonstrate the use of the filter.
# First make some data to be filtered.

# "Noisy" data.  We want to recover the 1.2 Hz signal from this.
#>data = np.sin(1.2*2*np.pi*t) + 1.5*np.cos(9*2*np.pi*t) + 0.5*np.sin(12.0*2*np.pi*t)

#with open('test.txt') as f:
with open('Empuje/'+textFile) as f:
    dataIn = f.read().splitlines() 
data=[]
sizeofData=len(dataIn)
t = np.linspace(0, sizeofData/1000, sizeofData, endpoint=False)
for i in dataIn:
    data.append(float(i))


# Filter the data, and plot both the original and filtered signals.
y = butter_lowpass_filter(data, cutoff, fs, order)


plt.subplot(2, 1, 2)
plt.plot(t, data, 'b-', label='data')
plt.plot(t, y, 'g-', linewidth=2, label='filtered data')
plt.xlabel('Time [sec]')
plt.grid()
plt.legend()

plt.subplots_adjust(hspace=0.35)
plt.show()


plt.plot(t, y, 'g-', linewidth=2)
plt.xlabel('Time [sec]')
plt.grid()
plt.legend()
plt.show()

f=open('Empuje/'+textSave,'a')

for x in y:
    #print(str(x)+'\n')
    f.write(str(x)+'\n')
f.close()