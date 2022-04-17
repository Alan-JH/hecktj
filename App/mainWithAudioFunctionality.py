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
import os, time

print(time.perf_counter())
r = sr.Recognizer()
print(time.perf_counter())
while done == False:
    with sr.Microphone() as source:
        print(time.perf_counter())
        print("Recording")
        # read the audio data from the default microphone
        audio_data = r.record(source, duration=5)
        print("Recognizing...")
        # convert speech to text
        try:
            text = r.recognize_google(audio_data)
            done = True
        except:
            pass
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

symptomDescription = pd.read_csv('Data/symptom_Description.csv')
symptomPrecaution = pd.read_csv('Data/symptom_precaution.csv')

with open("diagnosis.txt","a") as f:
    for output in outputs:
        f.write((symptomDescription.loc[symptomDescription['Disease']==output]).iat[0,1])
        f.write((symptomPrecaution.loc[symptomPrecaution['Disease']==output]).iat[0,1])

with open('diagnosis.txt', 'r') as f:
    inpText = f.read().replace('\n', ' ')




#########

CHUNK = 1024

PyAudio = pyaudio
language = 'en'


inputText = inpText
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
