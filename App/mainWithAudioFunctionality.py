import sys
from predict import Predictor

import speech_recognition as sr
import pyaudio


import pyaudio
import wave
import sys
import time

from gtts import gTTS
from playsound import playsound
import os


r = sr.Recognizer()
with sr.Microphone() as source:
    # read the audio data from the default microphone
    audio_data = r.record(source, duration=5)
    print("Recognizing...")
    # convert speech to text
    text = r.recognize_google(audio_data)
    # text = " ".join(sys.argv[1:])
    # print(text)

#######

predictor = Predictor()
output = predictor.filterText(text)
result = "Symptoms:"
for o in output:
    result += " " + o[0] + " (" + str(int(100*o[1])) + "%) "

with open("diagnosis.txt", "w") as f:
    f.write(result)
    f.write("\n")

symptoms = [s[0] for s in output]
output = predictor.processOutput(list(predictor.predict(symptoms).flatten()))

result = "Possible Diagnoses:"
for o in output:
    result += " " + o[0] + " (" + str(int(100*o[1])) + "%) "

with open("diagnosis.txt", "a") as f:
    f.write(result)


#########

CHUNK = 1024

PyAudio = pyaudio
language = 'en'


inputText = result
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
