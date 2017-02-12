import json
from watson_developer_cloud import NaturalLanguageClassifierV1


class getTopAction():
    def __init__(self):
        self.natural_language_classifier = NaturalLanguageClassifierV1(
                username='3e9259ef-e431-4cdd-a772-ecb5ffde30c6',
                password='gizBDtlWhOJg')
        self.classifierID = '2a3173x97-nlc-3599'

    def train_data(self):
        with open('./slideAction.csv', 'rb') as training_data:
            classifier = self.natural_language_classifier.create(
                    training_data=training_data,
                    name='SlideClassifier',
                    language='en'
            )
        json.dumps(classifier, indent=2)
        return classifier

    def get_classifiers(self, input_string):
        classes = self.natural_language_classifier.classify(self.classifierID, input_string)
        print(json.dumps(classes, indent=2))

    def get_top_classifier(self, input_string):
        classes = self.natural_language_classifier.classify(self.classifierID, input_string)
        return classes['classes'][0]


# print(json.dumps(classifier, indent=2))

# get_status()
# get_classifiers("next slide")

a = getTopAction()
# a.get_classifiers('previous slide')
print a.get_top_classifier('previous slide')
