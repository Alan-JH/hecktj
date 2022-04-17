import csv

symptoms = set()
DiseaseToSymptom = {}

with open( 'dataset.csv' , newline='' ) as csvfile :
    myreader = csv.reader( csvfile , delimiter=',' , quotechar='"' )
    # header
    for row in myreader :
        break
    # data
    for row in myreader :
        ls = [s for s in row[1:] if len(s) > 0]
        if row[0] not in DiseaseToSymptom.keys():
            DiseaseToSymptom[row[0]] = set(ls)
        else:
            DiseaseToSymptom[row[0]] = DiseaseToSymptom[row[0]].union(set(ls))
        symptoms = symptoms.union(set(ls))

print(symptoms)
print(DiseaseToSymptom)