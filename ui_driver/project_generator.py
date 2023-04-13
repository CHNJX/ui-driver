# -*- coding:utf-8 -*-
# @Time     :2023/2/2 10:41 下午
# @Author   :CHNJX
# @File     :project_generator.py
# @Desc     :项目创造器

import sys
from os import listdir
from os.path import dirname, exists, join

sys.path.append(dirname(sys.path[0]))

from ui_driver.template import Template
from ui_driver import ui_utils


class ProjectGenerator:
    def project_generate(self, project_name: str, project_type: str):
        """
        创建项目
        :param project_type: 项目类型 web/app
        :param project_name: 项目名称
        :return: None
        """
        if exists(project_name):
            print(f'project {project_name} is already existed')
            return 1
        ui_utils.create_folder(project_name)
        ui_utils.create_folder(join(project_name, 'testcase'))
        ui_utils.create_folder(join(project_name, 'page'))
        ui_utils.create_folder(join(project_name, 'base'))
        for dir_name in listdir(project_name):
            cur_dir = join(project_name + '/' + dir_name, '__init__.py')
            ui_utils.write("", cur_dir)

        self.__generate_base_need(project_name, project_type)

    def __generate_base_need(self, project_name, project_type: str):
        template = Template()
        base_dir = join(project_name, 'base')
        ui_utils.write(template.get_content('base_page.tpl'), join(base_dir, 'base_page.py'))
        if project_type == 'web':
            ui_utils.write(template.get_content('web.tpl'), join(base_dir, 'web.py'))
        else:
            ui_utils.write(template.get_content('web.tpl'), join(base_dir, 'web.py'))


if __name__ == '__main__':
    pass
