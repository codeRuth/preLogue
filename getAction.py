import json
from watson_developer_cloud import NaturalLanguageClassifierV1


class getTopAction:
    def __init__(self):
        self.natural_language_classifier = NaturalLanguageClassifierV1(
            username='c752b39e-808e-41d8-915d-d8348f34f56e',
            password='AOZdVQ718jzW')
        self.classifierID = 'f5b42ex171-nlc-3393'

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
        try:
            classes = self.natural_language_classifier.classify(self.classifierID, input_string)
            return classes['classes'][0]
        except:
            print "Connection Timeout."
