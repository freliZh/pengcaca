#!/usr/bin/env python
# -*-coding: utf-8 -*-
__author__ = 'livvy'

import tornado.web
import tornado.options
import tornado.httpserver
import tornado.ioloop
import torndb
import os.path
import controller.home
import controller.account
import controller.question
import logging
import config
import controller.test
import loggingConfig

__all__ = ['Application']

tornado.options.define("port", default=8888, help="run the given port",
                       type=int)


class Application(tornado.web.Application):
    def __init__(self):
        self.announce = controller.test.Announce()
        handlers = [
            (r"/", controller.home.HomeHandler),
            (r"/account/login", controller.account.LoginHandler),
            (r"/account/logout", controller.account.LogoutHandler),
            (r"/account/register", controller.account.RegisterHandler),
            (r"/question/ask", controller.question.AskHandler),
            (r"/question/show/([\d]+)", controller.question.ShowHandler),
            (r"/home/myPage",controller.home.myPageHandler),
            (r"/home/test",controller.test.MainHandler),
            (r"/home/test/chat",controller.test.ChatHandler),
            (r"/home/test/status",controller.test.StatusHandler)
        ]
        settings = dict(
            site_title=u"PengChaCha",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookie=True,
            cookie_secret="傻羊ASFfgshhajHJkwiqksmsKKd_asjjksaLsesdl",
            login_url="/account/login",
            debug=True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)
        self.db = torndb.Connection(
            host=config.SiteConfig.get('database',
                                       'host') + ':' + config.SiteConfig.get(
                'database', 'port'),
            database=config.SiteConfig.get('database', 'db'),
            user=config.SiteConfig.get('database', 'user'),
            password=config.SiteConfig.get('database', 'password'))


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    logging.getLogger("site").info("start")
    main()

