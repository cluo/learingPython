#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
实现多进程同时写一个文件功能

"""
import os.path
import logging
from mlogging import FileHandler_MP, TimedRotatingFileHandler_MP
from functools import partial

class LevelFilter(logging.Filter):

    def __init__(self, level, *args, **kwargs):
        #super(LevelFilter, self).__init__(*args, **kwargs)
        self.level = level

    def filter(self, record):
        return record.levelno == self.level

def init_info_logger(name, logging_dir):
    if not os.path.exists(logging_dir):
        os.makedirs(logging_dir)
    logging_file = os.path.join(logging_dir, name+".log")
    handler = TimedRotatingFileHandler_MP(logging_file, "midnight", 1,3)
    handler.setFormatter( logging.Formatter(
        "%(asctime)s %(levelname)-s %(message)s", #设置日志格式，固定宽度便于解析
        datefmt = "%Y-%m-%d %H:%M:%S" #设置asctime时间格式
    ))
    handler.suffix = "%Y%m%d"
    #只记录INFO级别信息，抛弃上面的WARNING、ERROR、CRITICAL几个级别
    handler.addFilter( LevelFilter(logging.INFO) )

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    #有些Python版本会报错KeyError，找不到clientip或user，这里用一个短横(-)做默认值
    extra={"clientip":"-", "user":"-"}
    #exc_info是出错时的Debug详细回溯信息，这里禁止记录，只记录错误信息这一行
    setattr(logger, "info", partial(logger.info, exc_info=False, extra=extra))
    logger.addHandler( handler )
    return logger

def init_error_logger(logging_dir):
    if not os.path.exists(logging_dir):
        os.makedirs(logging_dir)
    logging_file = os.path.join(logging_dir, "errors.log")
    handler = FileHandler_MP(logging_file)
    handler.setFormatter( logging.Formatter(
        "%(asctime)s %(levelname)-s %(message)s", #设置日志格式，固定宽度便于解析
        datefmt = "%Y-%m-%d %H:%M:%S" #设置asctime时间格式
    ))

    logger = logging.getLogger('errors')
    logger.setLevel(logging.WARNING)
    #有些Python版本会报错KeyError，找不到clientip或user，这里用一个短横(-)做默认值
    extra={"clientip":"-", "user":"-"}
    #exc_info是出错时的Debug详细回溯信息
    setattr(logger, "critical", partial(logger.critical, exc_info=False, extra=extra))
    setattr(logger, "error", partial(logger.error, exc_info=False, extra=extra))
    setattr(logger, "warning", partial(logger.warning, exc_info=False, extra=extra))
    logger.addHandler( handler )
    return logger

def init_data_logger(name, logging_dir):
    if not os.path.exists(logging_dir):
        os.makedirs(logging_dir)
    logging_file = os.path.join(logging_dir, name+".log")
    handler = TimedRotatingFileHandler_MP(logging_file, "midnight", 1,3)
    handler.setFormatter( logging.Formatter(
        "%(asctime)s %(message)s", #设置日志格式，固定宽度便于解析
        datefmt = "%Y-%m-%d %H:%M:%S" #设置asctime时间格式
    ))
    #只记录INFO级别信息，抛弃上面的WARNING、ERROR、CRITICAL几个级别
    handler.addFilter( LevelFilter(logging.INFO) )

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    #有些Python版本会报错KeyError，找不到clientip或user，这里用一个短横(-)做默认值
    extra={"clientip":"-", "user":"-"}
    #exc_info是出错时的Debug详细回溯信息，这里禁止记录，只记录错误信息这一行
    setattr(logger, "info", partial(logger.info, exc_info=False, extra=extra))
    logger.addHandler( handler )
    return logger

def init_sql_logger(name, logging_dir):
    if not os.path.exists(logging_dir):
        os.makedirs(logging_dir)
    logging_file = os.path.join(logging_dir, name+".log")
    handler = TimedRotatingFileHandler_MP(logging_file, "M", 1,4320)
    handler.setFormatter( logging.Formatter(
        "%(message)s", #设置日志格式，固定宽度便于解析
        datefmt = "%Y-%m-%d %H:%M:%S" #设置asctime时间格式
    ))
    handler.suffix = "%Y%m%d%M"
    #只记录INFO级别信息，抛弃上面的WARNING、ERROR、CRITICAL几个级别
    handler.addFilter( LevelFilter(logging.INFO) )

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    #有些Python版本会报错KeyError，找不到clientip或user，这里用一个短横(-)做默认值
    extra={"clientip":"-", "user":"-"}
    #exc_info是出错时的Debug详细回溯信息，这里禁止记录，只记录错误信息这一行
    setattr(logger, "info", partial(logger.info, exc_info=False, extra=extra))
    logger.addHandler( handler )
    return logger


def init_aps_logger(name, logging_dir):
    if not os.path.exists(logging_dir):
        os.makedirs(logging_dir)
    logging_file = os.path.join(logging_dir, name+".log")
    handler = TimedRotatingFileHandler_MP(logging_file, "D", 1, 30)
    handler.setFormatter( logging.Formatter('%(asctime)s %(levelname)s %(module)s.%(funcName)s Line:%(lineno)d %(message)s'))
    handler.suffix = "%Y%m%d%M"
    #只记录INFO级别信息，抛弃上面的WARNING、ERROR、CRITICAL几个级别
    handler.addFilter( LevelFilter(logging.INFO) )

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    #阻止日志向祖先hanlder传递
    logger.propagate = False
    #有些Python版本会报错KeyError，找不到clientip或user，这里用一个短横(-)做默认值
    extra={"clientip":"-", "user":"-"}
    #exc_info是出错时的Debug详细回溯信息，这里禁止记录，只记录错误信息这一行
    setattr(logger, "info", partial(logger.info, exc_info=False, extra=extra))
    logger.addHandler( handler )
    return logger

if __name__ == "__main__":
    #日志记录
    loggerInfo = init_info_logger(os.path.basename(os.path.realpath(__file__)).replace(".py",''), "./logs/")
    loggerError = init_error_logger("./logs/")
    # logger.info("test!")
