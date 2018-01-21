#!/usr/bin/env python3
from japronto import Application
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
    import logging
    db = initdb()
    app = Application()
    r = app.router
    r.add_route('/s/{p1}/', search)
    app.run(port=8888,debug=True)


def search(request):
    query_string=request.match_dict['p1']
    res = db.search(query_string)
    return request.Response(text=str())



if __name__ == "__main__":
    main()








# Requests with the path set exactly to `/` and whatever method
# will be directed here.
# def slash(request):
#     return request.Response(text='Hello {} /!'.format(request.method))
#
#
# r.add_route('/', slash)
#
#
# # Requests with the path set exactly to '/love' and the method
# # set exactly to `GET` will be directed here.
# def get_love(request):
#     return request.Response(text='Got some love')
#
#
# r.add_route('/love', get_love, 'GET')
#
#
# # Requests with the path set exactly to '/methods' and the method
# # set to `POST` or `DELETE` will be directed here.
# def methods(request):
#     return request.Response(text=request.method)
#
#
# r.add_route('/methods', methods, methods=['POST', 'DELETE'])


# Requests with the path starting with `/params/` segment and followed
# by two additional segments will be directed here.
# Values of the additional segments will be stored inside `request.match_dict`
# dictionary with keys taken from {} placeholders. A request to `/params/1/2`
# would leave `match_dict` set to `{'p1': 1, 'p2': '2'}`.


# from tornado.web import Application, RequestHandler
# from tornado.ioloop import IOLoop
# from DB import DB
#
#     app = Application([
#         (r"/s/(.+)", SearchHandler, dict(db=db)),
#     ])
#     app.listen(8888)
#     logging.info("will listen 8888")
#     IOLoop.current().start()
#
#
#
#
#
# class SearchHandler(RequestHandler):
#     def initialize(self, db):
#         self.db = db
#
#     def get(self, query_string):
#
#         r = self.db.search(query_string)
#         self.write(dict(size=len(r), entries=r))
