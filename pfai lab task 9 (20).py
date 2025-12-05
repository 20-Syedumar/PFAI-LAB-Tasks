import nltk
import random
from nltk.corpus import names
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy

nltk.download("names")


name_data = []

for file_id in names.fileids():
    gender_label = file_id.split(".")[0]
    for person_name in names.words(file_id):
        name_data.append((person_name.lower(), gender_label))

random.shuffle(name_data)

def create_features(name):
    result = {
        "last_letter": name[-1],
        "first_letter": name[0],
        "length": len(name)
    }
    return result

dataset = [(create_features(nm), gender) for nm, gender in name_data]

train_data = dataset[:4000]
test_data = dataset[4000:]


gender_classifier = NaiveBayesClassifier.train(train_data)

print("Model Accuracy:", accuracy(gender_classifier, test_data))

gender_classifier.show_most_informative_features(10)

new_name = "Ayesha"
new_features = create_features(new_name.lower())
print("Predicted Gender:", gender_classifier.classify(new_features))
