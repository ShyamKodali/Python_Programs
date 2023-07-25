#pip install sounddevice before importing 


import sounddevice 
import scipy 
from scipy.io.wavfile import write

# Sample Rate 
fs = 44100

# Input Recording Time 

time = int(input("Enter the time (in seconds) for Recording: "))
print("Recording started......\n")
record = sounddevice.rec(int(time * fs), samplerate=fs,channels=1)
sounddevice.wait()
write("MyRecording.wav", fs, record)
print("Recording is done please check your folder to listen recording")

