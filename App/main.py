import sys
from predict import Predictor
from data import SEVERITY, SEVERE_THRESHOLD

import speech_recognition as sr
import pyaudio
import pandas as pd

import pyaudio
import wave
import sys
import time

from gtts import gTTS
from playsound import playsound
import os, time

done = False
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
avgseverity = sum([SEVERITY[i] for i in symptoms])/len(symptoms)

if avgseverity > SEVERE_THRESHOLD:
    if avgseverity > 8:
        with open("diagnosis.txt", "a") as f:
            f.write("These are extremely severe symptoms\n")
    elif avgseverity > 5:
        with open("diagnosis.txt", "a") as f:
            f.write("These are severe symptoms\n")
    else:
        with open("diagnosis.txt", "a") as f:
            f.write("These are moderate symptoms\n")

    output = predictor.processOutput(list(predictor.predict(symptoms).flatten()))

    result = "Possible Diagnoses:"
    for o in output:
        result += " " + o[0] + " (" + str(int(100*o[1])) + "%) "

    with open("diagnosis.txt", "a") as f:
        f.write(result)

    symptomDescription = pd.read_csv('Data/symptom_Description.csv')
    symptomPrecaution = pd.read_csv('Data/symptom_precaution.csv')
else:
    print("These are mild symptoms, moving on without diagnosis", file = open("diagnosis.txt"))

#########

CHUNK = 1024

PyAudio = pyaudio
language = 'en'

with open("diagnosis.txt", "r")
    inpText = f.read().replace('\n', ' ')
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

##########





with open("diagnosis.txt","w") as f:
    for o in output:
        f.write("\n Would you like to hear a description of "+ o[0] + " and a reccomeneded precaution to take when dealing with it? Please just say yes, or no.")
        # f.write("\n If you think you have " + o[0] + "then we reccomend that you take the following precaution \n")
        # f.write((symptomPrecaution.loc[symptomPrecaution['Disease']==o[0]]).iat[0,1])
        # f.write("\n What is " + o[0] + "exactly, you may ask. Well, I'd be glad to tell you! \n")
        # f.write((symptomDescription.loc[symptomDescription['Disease']==o[0]]).iat[0,1])
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

        done = False
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
        
        if text.lower() == "yes":
            f.truncate(0)
            f.seek(0)
            f.write("\n If you think you have " + o[0] + "then we reccomend that you take the following precaution \n")
            f.write((symptomPrecaution.loc[symptomPrecaution['Disease']==o[0]]).iat[0,1])
            f.write("\n What is " + o[0] + "exactly, you may ask. Well, I'd be glad to tell you! \n")
            f.write((symptomDescription.loc[symptomDescription['Disease']==o[0]]).iat[0,1])
        else:
            f.truncate(0)
            f.seek(0)

        
        

