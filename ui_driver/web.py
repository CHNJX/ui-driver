# -*- coding:utf-8 -*-
# @Time     :2022/7/30 10:09 上午
# @Author   :CHNJX
# @File     :web.py
# @Desc     :web基类

from ui_driver.base_page import BasePage


class Web(BasePage):

    def teardown(self):
        self.driver.close()
