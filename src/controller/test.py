
import tornado.web
import tornado.websocket
import tornado.httpserver
import tornado.ioloop
import tornado.options

import json

class Announce():
    subject = "nima"
    callbacks = []

    def register(self, callback):
        self.callbacks.append(callback)

    def unregister(self, callback):
        self.callbacks.remove(callback)

    def getJson(self):
        return json.dumps({'content':self.subject})


    def changeSubject(self, data):
        self.subject = data
        self.notifyCallbacks()

    def notifyCallbacks(self):
        for c in self.callbacks:
            self.callbackHelper(c)


    def callbackHelper(self, callback):
        callback(self.getJson())

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("home/test.html")

class ChatHandler(tornado.web.RequestHandler):
    def post(self):
        content = self.get_argument('content')
        self.application.announce.changeSubject(content)

class StatusHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        self.application.announce.register(self.callback)

    def on_close(self):
        self.application.announce.unregister(self.callback)

    def on_message(self, message):
        pass

    def callback(self, data):
        self.write_message(data)