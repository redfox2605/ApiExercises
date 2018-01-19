from collections import defaultdict
from importlib.machinery import SourceFileLoader
#foo = SourceFileLoader("Record", "/Users/redfox/IdeaProjects/getYourGuide/de_code_challenge-a/Record.py").load_module()
#foo.Record()

class Record(object):
    def create(self,review_id, datee="", message=""):
        self.review_id = review_id
        self.datee = datee
        self.message = message



class DB(object):

    def __init__(self, entries=None):

        self.wordDict = defaultdict(list)
        self.recordsDict = defaultdict(Record)
        self.entries = [] if entries is None else entries


    def get_record_dict(self):
        return self.recordsDict
    def search(self, query_string):
        """
        >>> DB([(1, "", "tour city",), (2, "", "some other",)]).search("city tour")
        [(1, '', 'tour city')]
        """
        terms = query_string.split()
        print("searching {0}".format(terms))
        result = []
        print(len(self.entries))

        for e in self.entries:
            target = len(terms)
            for t in terms:
                if t in e[2]:
                    target -= 1
            if target == 0:
                result.append(e)
        print("result {0}".format(result))
        return result

    def add(self, entry):
        """
        >>> entry[0] == ""
        False
        """
        #self.entries.append(entry)
        "An entry is a tuple of (id, datatime, text)."
        id = entry[0]
        datee = entry[1]
        text = entry[2]
        self.recordsDict[id].create(id, datee, text)
        #for word in text.split():
        #    self.wordDict[word] += [id]

    def search(self,key_words):
        print(key_words)
        return ["hola","que tal"]