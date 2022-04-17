# hecktj
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


