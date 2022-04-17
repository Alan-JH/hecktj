import sys
from predict import Predictor
text = " ".join(sys.argv[1:])

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