#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from byecha.web.web import WebProcess

import os
from tornado.options import define, options
from tornado.options import parse_command_line, parse_config_file
from tornado.web import Application
from tornado.ioloop import IOLoop

define('port', type=int, default=8390, help='port number')
define('bind', type=str, default='127.0.0.1', help='binding address')
define("debug", type=bool, default=False, help="run in debug mode")
define("config", type=str, default="web.conf", help="config file")
define("proc_num", default=0, help="number of sub-processes(0:auto)", type=int)


def main():
    parse_command_line()
    if options.config and os.path.exists(options.config):
        parse_config_file(options.config)
    parse_command_line()

    web = WebProcess(port=options.port,
                     address=options.bind,
                     debug=options.debug,
                     proc_num=options.proc_num)

    web.start()

    web.join()


if __name__ == '__main__':
    main()
