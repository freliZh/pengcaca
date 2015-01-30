#!/usr/bin/env python
# -*-coding: utf-8 -*-
__author__ = 'zy'

import tornado.web
import base
import logging

#ask for a tutorial
class AskHandler(base.BaseHandler):
    @tornado.web.asynchronous
    def post(self, *args, **kwargs):
        user_id = self.get_secure_cookie("pengchacha-user")
        if not user_id:
            self.redirect("/account/login")
            return

        quest_title = self.get_argument("quest_title", None)
        quest_content = self.get_argument("quest_content", None)

        try:
            quest = self.db.execute("insert into question (user_id,question,description,time) values (%s,%s,%s,%s)",user_id,quest_title,quest_content,self.get_current_time())
        except Exception, e:
            print "insert erro!"
            logging.getLogger("site").error(e)

        #获取问题id
        quest_id = self.db.get("select max(id) as q_id from question where user_id = %s", int(user_id))

        url = "/question/show/" + str(quest_id['q_id'])
        self.redirect(url)

        self.finish()
        return
#用于展示用户请求的教程
class ShowHandler(base.BaseHandler):
    @tornado.web.asynchronous
    def get(self, quest_id):
        quest = self.db.get("select * from question where id = %s",quest_id)
        return self.render("question/show.html",quest_title=quest['question'],quest_content = quest['description'])

