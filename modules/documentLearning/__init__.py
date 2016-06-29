from .jsonExtractor import *
from .jsonSoftPro import *
import json
import nltk
from nltk.probability import *
import random
from nltk.corpus import names
from nltk.probability import DictionaryProbDist

config = {
    'wantdiff': False,
    'wantsfiles': False,
    'threadsafe': False,
    'behavior': {
        'creates': [['', '']],
        'uses': [['', '']]
    }
}

def run(context):

    all = []
    all2 = []
    all3 = []
    all4 = []
    all5 = []
    nochSoEine = []
    predModFinal = []

    json_data = jsonExtractor.getJsonData()
    for i in json_data:
        with open(getcwd() + "/modules/documentLearning/wiki-content.json") as json_file:
            data = json.load(json_file)
    namespaces = jsonSoftPro.getNamespaces(data)

    # This function is a getter for Namespaces and Features we are looking for within a json data
    # and returns us a "featureset" consisting of the namespace and the sections for it as list.
    def giv(json):
        for sec in json:
            if len(json_data) == len(all):
                break
            labeled_names = ([(elem, sec) for elem in json])
            featuresets = [(jsonSoftPro.getNamespaces(json), find_features(json)) for (n, s) in labeled_names]
            all.append(featuresets)
        return all


    # This function is return the sectionnames within the json data
    def find_features(json):
        t = jsonSoftPro.getSectionnames(json)
        return t


    # sums up the namespaces with their sections and returns them as list
    def test(input):
        neueListe2 = []
        finalList = []
        for pg in namespaces:
            neueListe = []
            for entry in input:
                le = entry[0]
                if (le['Namespace'] == pg):
                    neueListe.append(entry)
            neueListe2.append(neueListe)
        list2 = [x for x in neueListe2 if x != []]
        tmp = predModExtractor(list2)

        print(tmp)
        finalList.append(tmp)


    # Creates Prediction Model with NaiveBayes-Algorithm
    def predModExtractor(neueListe):
        predMod = []
        for k in neueListe:
            random.shuffle(k)
            train_set = k[:5]
            test_set = k[5:]
            classifier = nltk.NaiveBayesClassifier.train(train_set)
            nltk.classify.accuracy(classifier, test_set)
            d2 = classifier.prob_classify({'Namespace': 'Concept'})
            t = d2.samples()

            # We decided that sections under 10 percent are sorted out
            for l in t:
                if d2.prob(l) > 0.1:
                    print({l: d2.prob(l)})
                    predMod.append(l)
        return predMod


    # in progress
    def tester(json_data):
        for i in json_data:
            nsFile = jsonSoftPro.getNamespaces(i)
            namesFile = jsonSoftPro.getFileName(i)
            sFile = jsonSoftPro.getSectionnames(i)

        return


    # Creates a list of tuples. Each tuple consists of the namespace and one of its sections
    def transform(flattened2):
        l = 0
        k = 1
        z = 0
        i = 0

        for bla in flattened2:

            for bla in flattened2:

                try:
                    t = (flattened2[k][z], flattened2[l][0])
                    t = tuple(t)
                    all3.append(t)

                    z = z + 1
                    f = z

                except:
                    z = z - f
                    k = k + 2
                    l = l + 2
        return all3



    for i in json_data:
        giv(i)
    lf = giv(i)
    lf2 = giv(i)
    flattened = [val for sublist in lf for val in sublist]
    flattened2 = [val for sublist in flattened for val in sublist]
    all4 = transform(flattened2)
    for (n, s) in all4:
        s = ({'Namespace': s}, n)
        all5.append(s)
    test(all5)

    # tester(json_data)
