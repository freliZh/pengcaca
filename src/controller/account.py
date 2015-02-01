#!/usr/bin/env python
# -*-coding: utf-8 -*-
__author__ = 'livvy'

import tornado.web
import base
import logging

__all__ = ['LoginHandler', "RegisterHandler", 'LogoutHandler']


class LoginHandler(base.BaseHandler):
    @tornado.web.asynchronous
    def get(self, *args, **kwargs):
        return self.render("account/login.html")

    @tornado.web.asynchronous
    def post(self, *args, **kwargs):
        username = self.get_argument("username", None)
        password = self.get_argument("password", None)
        if not username or not password:
            return
        user = self.db.get("""select * from user where name = %s and
            password = %s and status = 1""", username, password)
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
    def get(self,*args, **kwargs):
        self.clear_cookie("pengchacha-user")
        self.render("account/register.html")

    def post(self, *args, **kwargs):
        username = self.get_argument("username")
        password = self.get_argument("password")
        phone_number = self.get_argument("phone_number")
        address = self.get_argument("address")

        try:
            user = self.db.execute("insert into user (name,password,phone_number,address_1,register_date) "
                                   "values (%s,%s,%s,%s,%s)",username,password,phone_number,address,self.get_current_time())
        except Exception, e:
            print "insert user table error!"
            logging.getLogger("site").error(e)

        #获取user_id
        user = self.db.get("select max(id) as user_id from user where name = %s", username)
        if user:
            print user
        self.set_secure_cookie("pengchacha-user", str(user['user_id']))
        self.redirect("/")



