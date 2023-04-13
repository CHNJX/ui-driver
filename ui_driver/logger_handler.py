# -*- coding:utf-8 -*-
# @Time     :2022/8/1 15:12
# @Author   :CHNJX
# @File     :logger_handler.py
# @Desc     :日志收集器
import logging
import os
import sys
import time
from datetime import datetime


class LoggerHandler:
    workdir = os.path.split(os.path.realpath(__file__))[0]

    @classmethod
    def get_logger(cls, name, root_path, package_name="log") -> logging:
        """
        获取日志控制器
        :param root_path: 项目根目录
        :param name: 日至控制器名称
        :param package_name: 存放的包名
        """
        logger = logging.getLogger(name)
        if logger.handlers:
            return logger
        logger.setLevel(logging.DEBUG)
        now_string = datetime.now().strftime('%Y%m%d')
        file_name = f'{now_string}_log.log'
        logger_dir = os.path.join(root_path, package_name)
        if not os.path.exists(logger_dir):
            os.mkdir(logger_dir)
        file_path = os.path.join(logger_dir, file_name)
        t = int(time.time())

        # FileHandler
        fh = logging.FileHandler(file_path, mode='a', encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            '******%(asctime)s - %(name)s - %(filename)s,line %(lineno)s - %(levelname)s: %(message)s')
        fh.setFormatter(formatter)

        sh = logging.StreamHandler(sys.stdout)
        sh.setFormatter(formatter)
        sh.setLevel(logging.DEBUG)
        logger.addHandler(fh)
        logger.addHandler(sh)

        return logger