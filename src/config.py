#!/usr/bin/env python
# -*-coding: utf-8 -*-
__author__ = 'livvy'

import ConfigParser

__all__ = ['SiteConfig']


class SiteConfig:
    def __init__(self):
        pass

    __all_config = ConfigParser.ConfigParser()
    __all_config.read("config.ini")

    @staticmethod
    def get(section, option):
        return SiteConfig.__all_config.get(section, option)

    @staticmethod
    def getboolean(section, option):
        return SiteConfig.__all_config.getboolean(section, option)

    @staticmethod
    def getint(section, option):
        return SiteConfig.__all_config.getint(section, option)

    @staticmethod
    def getfloat(section, option):
        return SiteConfig.__all_config.getfloat(section, option)


if __name__ == "__main__":
    port = SiteConfig.get("database","port")
    print port
