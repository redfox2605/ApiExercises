#!/usr/bin/env python3
from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
from DB import DB
def main():
    import logging
    db = initdb()
    app = Application([
        (r"/s/(.+)", SearchHandler, dict(db=db)),
    ])
    app.listen(8888)
    logging.info("will listen 8888")
    IOLoop.current().start()



def initdb(filename="data.json"):
    import json

    db = DB()
    with open(filename, "r", encoding='utf-8-sig') as f:
        for l in f:
            q_dict = json.loads(l)
            for e in q_dict["data"]:
                db.add((e['review_id'], e['date'], e['message']))
    return db

class SearchHandler(RequestHandler):
    def initialize(self, db):
        self.db = db

    def get(self, query_string):
        r = self.db.search(query_string)
        self.write(dict(size=len(r), entries=r))

if __name__ == "__main__":
    main()
