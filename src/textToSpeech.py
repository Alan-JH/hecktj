import pyaudio
import wave
import sys
import time

from gtts import gTTS
from playsound import playsound
import os

CHUNK = 1024

if len(sys.argv) < 2:
    sys.exit(-1)
PyAudio = pyaudio
language = 'en'

if sys.argv[1][-3] == '.wav':
    print("Inputted a file.")
    print("Playing " + sys.argv[1])
    wavFile = wave.open(sys.argv[1], 'rb')

else:
    inputText = sys.argv[1]
    speechObj = gTTS(text=inputText,lang=language,slow=False)
    speechObj.save("outputVoice.wav")
    playsound('outputVoice.wav')
    wavFile = wave.open("outputVoice.wav",'rb')

p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(wavFile.getsampwidth()),
                    channels=wavFile.getnchannels(),
                    rate=wavFile.getframerate(),
                    output=True)

data = wavFile.readframes(CHUNK)

while data != '':
        stream.write(data)
        data = wavFile.readframes(CHUNK)

stream.stop_stream()
stream.close()

p.terminate()
