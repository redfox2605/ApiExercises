from collections import defaultdict
import re

class Record(object):
    def create(self,review_id, datee="", message=""):
        self.review_id = review_id
        self.datee = datee
        self.message = message

    def getTuple(self):
        return self.review_id, self.datee, self.message


class DB(object):

    def __init__(self, entries=None):

        self.wordDict = defaultdict(set)
        self.recordsDict = defaultdict(Record)
        if entries is not None:
            self.add_fromList(entries)

    def add_fromList(self, entries):
        for e in entries:
            self.add(e)

    def printWordDict(self):
        for k,v in self.wordDict.items():
            print("k:{0} ->  {1}".format(k, v))

    def get_record_dict(self, id):
        return self.recordsDict[id]

    def search(self, query_string):
        """
        >>> DB([(1, "", "tour city",), (2, "", "some other",)]).search("city tour")
        [(1, '', 'tour city')]
        """
        terms = query_string.lower().split()
        result = set(self.wordDict[terms[0]])
        if len(result) == 0:
            return list()
        else:
            for t in terms[2:]:
                records_containing_t = self.wordDict[t]
                result = result.intersection(records_containing_t)
            return [self.get_record_dict(id).getTuple() for id in result]



        #for e in self.entries:
        #    target = len(terms)
        #    for t in terms:
        #        if t in e[2]:
        #            target -= 1
        #    if target == 0:
        #        result.append(e)
        #print("result {0}".format(result))

    def add(self, entry):
        """
        Test to check if everything has been indexed correctly
        >>> DB([(1, "", "tour city",), (2, "", "some other",)]).recordsStoredCount()
        2
        >>> DB([(1, "", "tour city",), (2, "", "some other",)]).indexedWordsCount()
        4
        """
        "An entry is a tuple of (id, datatime, text)."
        id = entry[0]
        datee = entry[1]
        text = re.sub('[^A-Za-z0-9]+', ' ', entry[2].lower())
        self.recordsDict[id].create(id, datee, entry[2])
        for word in text.split():
            self.wordDict[word].add(id)


    def indexedWordsCount(self):
        return len(self.wordDict)

    def recordsStoredCount(self):
        return len(self.recordsDict)
