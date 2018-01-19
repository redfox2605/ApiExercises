from collections import defaultdict


class Record(object):
    def create(self,review_id, datee="", message=""):
        self.review_id = review_id
        self.datee = datee
        self.message = message



class DB(object):

    def __init__(self, entries=None):

        self.wordDict = defaultdict(list)
        self.recordsDict = defaultdict(Record)
        if entries is not None:
            self.add_fromList(entries)

    def add_fromList(self, entries):
        for e in entries:
            self.add(e)

    def get_record_dict(self, id):
        return self.recordsDict[id]

    def search(self, query_string):
        """
        >>> DB([(1, "", "tour city",), (2, "", "some other",)]).search("city tour")
        [(1, '', 'tour city')]
        """
        terms = query_string.split()
        result = set()

        for t in terms:
            records_containing_t = self.wordDict[t]

            for id in records_containing_t:
                r = self.get_record_dict(id)
                result.add((r.review_id, r.datee, r.message))

        return list(result)

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
        text = entry[2]
        self.recordsDict[id].create(id, datee, text)
        for word in text.split():
            self.wordDict[word] += [id]

    def indexedWordsCount(self):
        return len(self.wordDict)

    def recordsStoredCount(self):
        return len(self.recordsDict)
