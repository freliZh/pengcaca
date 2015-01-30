#!/usr/bin/env python
# -*-coding: utf-8 -*-
__author__ = 'livvy'

import tornado.web
import base

__all__ = ['LoginHandler', "RegisterHandler", 'LogoutHandler']


class LoginHandler(base.BaseHandler):
    @tornado.web.asynchronous
    def get(self, *args, **kwargs):
        return self.render("account/login.html")

    @tornado.web.asynchronous
    def post(self, *args, **kwargs):
        email = self.get_argument("email", None)
        password = self.get_argument("password", None)
        if not email or not password:
            return
        user = self.db.get("""select * from user where email = %s and
            password = %s and status = 1""", email, password)
        if not user:
            self.redirect("/")
            return
        user_id = user["id"]
        self.set_secure_cookie("pengchacha-user", str(user_id))
        self.redirect(self.get_argument("next", "/"))
        self.finish()


class LogoutHandler(base.BaseHandler):
    def get(self, *args, **kwargs):
        self.clear_cookie("pengchacha-user")
        self.redirect("/")


class RegisterHandler(base.BaseHandler):
    def post(self, *args, **kwargs):
        email = self.get_argument("email")

