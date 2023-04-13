# -*- coding:utf-8 -*-
# @Time     :2023/4/13 9:56 下午
# @Author   :CHNJX
# @File     :test_startproject.py
# @Desc     :

from ui_driver.project_generator import ProjectGenerator

def test_starproject():
    ProjectGenerator().project_generate('ui_demo','web')


if __name__ == '__main__':
    test_starproject()