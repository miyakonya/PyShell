# coding: UTF-8
# Python 3.10.6
"""
你需要写日期和作者
Date:
By xxx
"""

"""
推荐参考exploit/resources/base_module.py文件
请将你的CVE模块文件放到exploit/ 目录
"""

from resources import shell
from resources.base_module import BaseExploit
from resources.font import print_error, print_success, print_info

"""
BaseExploit和shell必须导入
font为字体库，根据需要导入
"""

# 类名必须是Exploit，且要继承BaseExploit
class Exploit(BaseExploit):
    def __init__(self, host, port):
        # 调用__init__()以初始化
        super().__init__(host, port)
        """
        self.info和self.args请参考exploit/resources/base_module.py文件的注释
        """
        self.info = {

        }
        self.args = {

        }

    # 重写run方法，run方法是执行exploit代码的
    def run(self):
        pass
    # 列出模块参数的方法，通常可以直接用super()调用
    def options(self):
        super().options()
    # 设置模块参数的方法
    def set(self, arg, value):
        """
        内置有host和port参数，如果有需要可以拓展
        :param arg: 参数名
        :param value: 参数值
        """
        super().set(arg, value)
    # 列出作者信息(即self.info)的方法，直接用super()调用
    def show_info(self):
        super().show_info()
