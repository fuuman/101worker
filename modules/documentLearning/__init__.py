from .jsonExtractor import *
from .jsonSoftPro import *
import json
import nltk
import random
from os import getcwd

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
    # will get all entries of our Featureset in the function 'rawFeatureset
    allRawFeaturesets = []
    # this contains later on all tuples extracted of our rawFeatureset
    rfTupleList = []
    # this contains later on our list which can be interpreted by our machine learning algorithm
    finalFeatureset = []
    # gets us the list of the json data files in the projectfile. Each list entry is a string.
    json_data = jsonExtractor.getJsonData()

    #########################################################################################################################
    # This function returns us a raw "featureset" consisting of the namespace and the sections for it as list.
    # e.g. [[(['Concept'], ['Headline', 'Metadata', 'Description'])], [(['Technology'], ['Headline', 'Metadata'])],..]]
    # input is a single json data
    def rawFeatureset(json):
        # this for-loop extracts in each json data we give in the namespace and sectionname
        # and transforms it in a list we can use in further steps
        for sec in json:
            # if our allRawFeaturesets list is as long as the json_data we stop.
            # Due to problems the program read more data as it should, this seems to fix it
            if len(json_data) == len(allRawFeaturesets):
                break
            labeled_names = ([(elem, sec) for elem in json])
            featuresets = [(jsonSoftPro.getNamespaces(json), jsonSoftPro.getSectionnames(json)) for (n, s) in
                           labeled_names]
            allRawFeaturesets.append(featuresets)

        return allRawFeaturesets

    ########################################################################################################################
    #######################################################################################################################
    # "transform" transforms us our raw Featureset into a list our machine learning algorithm can deal with
    # e.g. [({'Namespace': 'Concept'}, 'Headline'), ({'Namespace': 'Concept'}, 'Description'),...
    def transform(allRawFeaturesets):
        # first we flatten our raw Featureset, till we got a simple nested list
        # [['Concept'], ['Metadata', 'Description', 'Headline'], ['Technology'], ['Metadata', 'Headline'],...]]
        flattened = [val for sublist in lf for val in sublist]
        flattened2 = [val for sublist in flattened for val in sublist]

        # this nested for-loop applies the namespace we have with each section of it as tuples
        # e.g. [('Description', 'Concept'), ('Headline', 'Concept'), ('Metadata', 'Concept'),..]
        l = 0
        k = 1
        z = 0
        for entry in flattened2:
            for entry in flattened2:
                # this try-catch block guarantees that we do not run out of bound within the list.
                # if we exceed the list length with our parameter z the except block will return our z to 0
                # and we can go on
                try:
                    t = (flattened2[k][z], flattened2[l][0])
                    t = tuple(t)
                    rfTupleList.append(t)

                    z = z + 1
                    f = z

                except:
                    z = z - f
                    k = k + 2
                    l = l + 2

        # this for-loop will transform every first tuple entry as a dictionary
        for (n, s) in rfTupleList:
            s = ({'Namespace': s}, n)
            finalFeatureset.append(s)
        return finalFeatureset

    #######################################################################################################################
    ########################################################################################################################
    # this function sorts our tuples by their namespaces
    # so that all namespaces are listed after another
    # e.g. first all tuples of 'Concept' and then all tuples of 'Technology'
    # this is a approach to compare our outcoming prediction model with lists of concepts and sections
    # in other json data. It is not useful by now.
    def sortByNamespaces(finalFeatureset):
        # we extract all namespaces out of the wiki-content.json
        # and save them as a list in namespace. We are just passing our finalFeatureset through, which is shuffled anyway
        # later on.
        for i in json_data:
            with open(getcwd() + "/modules/documentLearning/wiki-content.json") as json_file:
                data = json.load(json_file)
        namespaces = jsonSoftPro.getNamespaces(data)

        neueListe2 = []
        finalList = []
        for pg in namespaces:
            neueListe = []
            for entry in finalFeatureset:
                le = entry[0]
                if (le['Namespace'] == pg):
                    neueListe.append(entry)
            neueListe2.append(neueListe)
        list2 = [x for x in neueListe2 if x != []]
        tmp = predMod(list2)
        finalList.append(tmp)

    #######################################################################################################################
    #######################################################################################################################

    # Creates Prediction Model with NaiveBayes-Algorithm
    def predMod(finalFeatureset):
        predMod = []
        for k in finalFeatureset:
            # this step will mix up our finalFeatureset on test purposes
            random.shuffle(k)
            # the first 5 entries in our finalFeatureset will be used as training set for
            # our algorithm
            train_set = k[:5]
            # everything over the 5th entry will be tested on (not used)
            # test_set = k[5:]
            # our classifier is the Naive Bayes Classifier
            classifier = nltk.NaiveBayesClassifier.train(train_set)

            # nltk.classify.accuracy(classifier, test_set)
            # this line is just for "creating" a prob-object we can use, the input is not relevant
            d2 = classifier.prob_classify({'Namespace': 'Concept'})
            # the sampleList are all sectionnames in our trainigsset for a given Namespace
            sampleList = d2.samples()

            # We decided that sections under 10 percent are sorted out
            # e.g. is Illustration under 10 percent in our prediction it will not be in the list
            # which might look like ['Headline','Metadata',...]
            # this for-loop will also print out the probability for each section
            for l in sampleList:
                if d2.prob(l) > 0.1:
                    print({l: d2.prob(l)})
                    predMod.append(l)

                    # is printing our comparison list for the different namespaces we wanted to use for testing
            print({'List for comparison for tests': list(sampleList)})
        return predMod

    ########################################################################################################################
    ########################################################################################################################


    # in progress
    def tester(json_data):
        for i in json_data:
            nsFile = jsonSoftPro.getNamespaces(i)
            namesFile = jsonSoftPro.getFileName(i)
            sFile = jsonSoftPro.getSectionnames(i)

        return

    ########################################################################################################################
    #######################################################################################################################

    # main
    # reads in our list of json datas one json data after another passing it to rawFeatureset
    for i in json_data:
        rawFeatureset(i)
    # lf catches the list of all results of 'rawFeaturesets'
    lf = rawFeatureset(i)
    fF = transform(lf)
    sortByNamespaces(fF)


