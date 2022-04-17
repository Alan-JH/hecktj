# About HealthHonk

## Inspiration
We were inspired by voice assistants like Alexa and Siri and wanted to put a humanitarian twist on it. Thus sparked the idea of helping give medical advice with a voice assistant. 

## What it does
The project takes spoken symptoms of a patient as input and uses a machine learning model to diagnose diseases. The app responds with a reiteration of all of the symptoms and lists the three most probable diseases associated with the symptoms alongside their respective probabilities. The app also gives descriptions of the diseases and the overall severity of the user's current condition.

## How we built it
We used Tensorflow to train the machine learning model that predicts diseases based on symptoms of a patient. We also used python tkinter for our graphical interface. Several other libraries, like speech_recognition and pyaudio were also used to make our project a success.

## Challenges we ran into
We initially planned on hosting our project on a website, but due to the lack of sufficient cpu and ram when using a free repl.it account, we were unable to implement the machine learning aspect of our project into our website. We had to completely rework our user interface and instead switched to an app.

## Accomplishments that we're proud of
We are proud that everything came together and we were able to succesfully create a helpful product. We hope that the product will be useful and help those who are sick get the medical attention they need. Although our prediction algorithm is far from perfect we believe what we accomplished during the 24 hour time limit is quite commendable. 

## What we learned
While some of our members were experienced in machine learning algorithms the others had to learn as we went. None of us were very experienced in graphic design as well, so we learned a lot as we designed the front end for the user. We also learned how important efficiency is in coding as we experienced firsthand the issues of memory shortage when we had to switch to a python application.

## What's next for Health Honk
We would love to continue developing our product into a more compact app in the future. We also need to increase the overall accuracy of our disease detection algorithm. We see our technology as being the Amazon Alexa of the healthcare industry and we are excited to see where this mission will take us!

# Instructions For Installation:

1. Install the file titled App.zip from this google drive link: https://drive.google.com/drive/folders/1O6LatkEwcmqst92ecunQLtyf0rK1oCoo?usp=sharing
2. Unzip the App.zip file
3. Run install.sh or install.bat based on operating system to install dependencies like tensorflow or install them on your own.

**Instructions To Run On Mac***

1. Locate run.command in the App Folder
2. Inside the file edit the given path to the path where the "App" folder is located.
3. Open terminal and cd into the App Folder
4. type chmod +x run.command
5. Software is now setup!
6. Simply click run.command to test out our application

**Instructions To Run On Windows**

1. Locate the run.bat file in the App Folder
2. Software is now setup!
3. Double click this file to test our our application

**Instructions To Run On Linux***

1. Locate the run.sh file in the App Folder
2. Software is now setup!
3. Double click this file to test our our application

*Mac and Linux Versions Require homebrew installation: https://brew.sh/


# hecktj
Comments From Design Process **DISREGARD FOR INSTALLATION INSTRUCTIONS**
like, heccin tj, amirite dudes? totalllyyyyyy....

10Epoch: Folder with all saved model stuff

Data: Folder with the original data we used.

data.py: just includes lists of all possible symptoms and diseases

diagnosis.txt: When main.py is run, the diagnosis will be written to this file.

main.py: If you clone this repo, this is the only thing that needs to be run.

notebook.ipynb: used as a playground of sorts. This is where we processed the data in the Data folder into a format compatible with training our machine learning model(a model that predicts the disease you have based on symptoms). It is also where we trained said model.

predict.py: home of the Predictor class. Basically, this class has methods that deal with taking the text from the user, which is collected using speech-to-text code from our website, and determining what symptoms that patient has using a DIFFERENT machine learning model. It has a method that predicts what disease a patient has based on said symptoms, a method that uses the FIRST MACHINE LEARNING MODEL we made.

requestsToText.py and textToSpeech.py are somewhat outdated files, and probably will not play a role in our final implementation.

requirements.txt has requirements


