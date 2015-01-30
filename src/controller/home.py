#!/usr/bin/env python
# -*-coding: utf-8 -*-
__author__ = 'livvy'

import tornado.web
import base
import logging

__all__ = ['HomeHandler']


class HomeHandler(base.BaseHandler):
    def data_received(self, chunk):
        pass

    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        logging.getLogger("site").info("home page")
        user_id = self.get_secure_cookie("pengchacha-user")
        logging.getLogger("site").info(user_id)
        return self.render("home/index.html")

class myPageHandler(base.BaseHandler):

    @tornado.web.authenticated
    def get(self):
        user_id = self.get_secure_cookie("pengchacha-user")

        questions = self.db.query("SELECT * FROM question where user_id = %s ORDER BY time DESC ",int(user_id))
        answers = self.db.query("SELECT * FROM answers where user_id = %s ORDER BY time DESC ",int(user_id))

        self.render("home/myPage.html", questions=questions,answers = answers)
