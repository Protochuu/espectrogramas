from pydub import AudioSegment
from scipy.io import wavfile
import numpy as np 
import matplotlib.pyplot as plt
from scipy.signal import ShortTimeFFT
from scipy.signal.windows import gaussian


#song = AudioSegment.from_ogg('evaluacion_3.mp3')
#song.export('evaluacion_3.wav', format = 'wav')

samplerate,data = wavfile.read('evaluacion_3.wav')

length = data.shape[0]/samplerate  
time = np.linspace(0.,length, data.shape[0])
#plt.plot(time,data[:])
#plt.show()

g_std = 8
w = gaussian(50, std = g_std, sym = True)
SFT = ShortTimeFFT(w,hop=16, fs=samplerate, mfft=1024,scale_to='psd')
#Sx = SFT.spectrogram(data)
plt.specgram(data,Fs = samplerate,NFFT = 256, noverlap = 128, cmap = 'viridis' )
#fig1, ax1= plt.subplots(figsize = (6.,4.))
#t_lo,t_hi = SFT.extent(data.shape[0])[:2]
#im1 = ax1.imshow(Sx, cmap = 'magma', origin='lower', aspect='auto')


plt.show()
