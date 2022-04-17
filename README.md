
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


