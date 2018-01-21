#!/usr/bin/env python3
from japronto import Application
import logging
from DB import DB


db=DB()
def initdb(filename="data.json"):
    import json

    db = DB()
    with open(filename, "r", encoding='utf-8-sig') as f:
        for l in f:
            q_dict = json.loads(l)
            for e in q_dict["data"]:
                db.add((e['review_id'], e['date'], e['message']))
    #db.printWordDict()
    return db


def main():

    db = initdb()
    app = Application()
    r = app.router
    r.add_route('/s/{p1}/', search)
    app.run(port=8888)



def search(request):
    try:
        query_string=request.match_dict['p1']
        return request.Response(text=str(db.search(query_string)))
    except Exception as e:
        logging.error(e, exc_info=True)

if __name__ == "__main__":
    main()

