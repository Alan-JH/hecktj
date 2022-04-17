from tensorflow import keras
from data import DISEASES, SYMPTOMS
from sentence_transformers import SentenceTransformer, util
import numpy as np
import 

class Predictor:
    MODELNAME = "10Epoch"
    WORDSPERSYMPTOM = 4 # Estimated number of words per described symptom
    
    def __init__(self):
        self.model = keras.models.load_model(Predictor.MODELNAME)


    def filterText(self, badText): 
        """
        this is basically a really bad way of trying to determine what symptoms a person has based on the text we get from their speech.
        """
        badTextSymptomsFound = set()
        try:
            stupid_model = SentenceTransformer('distilbert-base-nli-mean-tokens')
        except HTTPError as e:
            print(e)
            time.sleep(.5)
            print("trying again")
            stupid_model = SentenceTransformer('distilbert-base-nli-mean-tokens')
        sentences = SYMPTOMS.copy()
        sentences.insert(0,badText)
        sentence_embeddings = stupid_model.encode(sentences)
        estimatedSymptoms = len(badText.split(" ")) / self.WORDSPERSYMPTOM
        processedSymptoms = [util.pytorch_cos_sim(sentence_embeddings[0], sentence_embeddings[i]) for i in range(1,len(sentence_embeddings))]
        thresh = 0.99
        temp = [i for i in processedSymptoms if i > thresh]
        while len(temp) < estimatedSymptoms:
            temp = [i for i in processedSymptoms if i > thresh]
            thresh -= 0.01
        return [(SYMPTOMS[processedSymptoms.index(i)], i) for i in temp]
    
    def predict(self, inlist):
        """
        Takes a list of strings that are in the symptoms set
        Returns a list of probabilities corresponding to DISEASES
        """
        inlist = np.array([[int(s in inlist) for s in SYMPTOMS]])
        output = self.model.predict(inlist)
        
        return output

    def processOutput(self, outlist):
        """
        Takes the list of probabilities, takes the top three most likely and their disease names
        """
        ls = outlist.copy()
        ls.sort()
        result = []
        for prob in ls[-3:]:
            result.append((DISEASES[outlist.index(prob)], prob))
        return result

    


# from sentence_transformers import SentenceTransformer, util

# model = SentenceTransformer('distilbert-base-nli-mean-tokens')

# sentences = SYMPTOMS.copy()
# sentences.insert(0,'i have a cough')
# sentence_embeddings = model.encode(sentences)
# print(sentences)
# # for sentence, embedding in zip(sentences, sentence_embeddings):
# #     print("Sentence:", sentence)
# #     print("Embedding:", embedding)
# #     print("")

# ls = []
# for i in range(1,len(sentence_embeddings)):
#     val = util.pytorch_cos_sim(sentence_embeddings[0], sentence_embeddings[i])
#     print(sentences[i], val)
#     ls.append(val)

# ls.sort()
# print(ls[-3:])