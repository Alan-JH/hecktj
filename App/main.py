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
import os, time, subprocess

def main():
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
        with open("diagnosis.txt", "a") as f:
            f.write("These are mild symptoms, moving on without diagnosis\n")

    #########

    CHUNK = 1024

    PyAudio = pyaudio
    language = 'en'

    with open("diagnosis.txt","a") as f:
        for o in output:
            f.write("\n If you think you have " + o[0] + "then we reccomend that you take the following precaution \n")
            f.write((symptomPrecaution.loc[symptomPrecaution['Disease']==o[0]]).iat[0,1])
            f.write("\n What is " + o[0] + "exactly, you may ask. Well, I'd be glad to tell you! \n")
            f.write((symptomDescription.loc[symptomDescription['Disease']==o[0]]).iat[0,1])
            

    with open('diagnosis.txt', 'r') as f:
        inpText = f.read().replace('\n', ' ')

    with open("diagnosis.txt", "r") as f:
        inpText = f.read().replace('\n', ' ')
        inputText = inpText
        speechObj = gTTS(text=inputText,lang=language,slow=False)
        speechObj.save("outputVoice.mp3")
        subprocess.call(['ffmpeg', '-y', '-i', 'outputVoice.mp3', 'outputVoice.wav'])
        playsound('outputVoice.wav')
        wavFile = wave.open("outputVoice.wav",'rb')