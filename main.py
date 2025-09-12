from pydub import AudioSegment
from scipy.io import wavfile
import numpy as np 
import matplotlib.pyplot as plt
from scipy.signal import ShortTimeFFT
from scipy.signal.windows import gaussian
import os 

os.makedirs("./converted", exist_ok=True)
os.makedirs("./audio", exist_ok=True)
os.makedirs("./spectrogram", exist_ok= True)

for root,dirs,files in os.walk("./audio"):
    for file in files:
        if not os.path.exists(file):
            print(f"Se está convirtiendo el archivo: {file}")
            song = AudioSegment.from_ogg(f"./audio/{file}")

            song_root,ext= os.path.splitext(file)
            song.export(f'./converted/{song_root}.wav', format = 'wav')

        samplerate,data = wavfile.read(f'./converted/{song_root}.wav')

        print(f"Espectograma de audio: {file} se está generando")
        plt.specgram(data,Fs = samplerate,NFFT = 256, noverlap = 128, cmap = 'viridis')

        print(f"Espectograma de audio: {file} generado")
        plt.savefig(f'./spectrogram/{song_root}.png')
