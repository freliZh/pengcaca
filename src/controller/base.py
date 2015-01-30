#!/usr/bin/env python
# -*-coding: utf-8 -*-

__author__ = 'livvy'

import tornado.web
import datetime

__all__ = ['BaseHandler']


class BaseHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    @property
    def db(self):
        return self.application.db

    def get_current_user(self):
        user_id = self.get_secure_cookie("pengchacha-user")
        if not user_id: return None
        return self.db.get("select * from USER where id = %s", int(user_id))

    @staticmethod
    def get_current_time():
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

