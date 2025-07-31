# coding:UTF-8
# Python 3.10.6
# PyShell的主程序
import importlib
from importlib import import_module
import os
import sys
from platform import system

from exploit.resources.font import print_error, print_info
# 添加必要的路径，避免导入模块时报错
module_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(module_dir)
sys.path.append(module_dir + "\\exploit")
sys.path.append(module_dir + "\\exploit\\resources")

current_dir = os.path.dirname(os.path.abspath(__file__))
modules_dir = os.path.join(current_dir, "exploit")
sys.path.insert(0, modules_dir)


class PyShell:
    def __init__(self):
        self.files = []
        self.module = None
        self.module_name = None
        self.exploit_path = modules_dir
        # 获取模块
        for item in os.listdir(self.exploit_path):
            full_path = os.path.join(self.exploit_path, item)
            if os.path.isfile(full_path) and item.endswith(
                    ".py") and item != "__init__.py":
                self.files.append(item[:-3])

    # show命令
    def show(self):
        for item in self.files:
            print(item)

    # use命令
    def use(self, module_name):
        try:
            self.module_name = module_name
            self.module = import_module(module_name).Exploit()
        except ModuleNotFoundError:
            print_error("Module not found: " + self.module_name)

    # 执行模块
    def run(self):
        try:
            self.module.run()
        except BaseException as e:
            print_error(e)

    # 查看模块选项
    def options(self):
        try:
            self.module.options()
        except BaseException as e:
            print_error(e)

    # 设置模块参数
    def set(self, arg, value):
        try:
            self.module.set(arg, value)
        except BaseException as e:
            print_error(e)

    def info(self):
        try:
            self.module.show_info()
        except BaseException as e:
            print_error(e)

    @staticmethod
    def arg_exploit(exploit, host, port):
        try:
            arg_exp = import_module(exploit).Exploit()
            arg_exp.set("host", host)
            arg_exp.set("port", port)
            arg_exp.run()
        except ModuleNotFoundError:
            print_error("Module not found: " + exploit)
        except TypeError:
            print_error("Missing parameters or module does not support calling as command-line parameters")

    def console(self):
        while True:
            if self.module:
                cmd = input(f"PyShell({self.module_name})> ").lower()
            else:
                cmd = input("PyShell> ").lower()
            cmdl = cmd.split(" ")
            if cmd == "show":
                self.show()
            elif cmd.startswith("use"):
                if len(cmdl) != 2:
                    print_error("Parameter error! Usage: use [module name]")
                    continue
                self.use(cmdl[1].upper())
            elif cmd == "run":
                if self.module is None:
                    print_error("You haven't used any modules yet!")
                    continue
                self.run()
            elif cmd == "options":
                if self.module is None:
                    print_error("You haven't used any modules yet!")
                    continue
                self.options()
            elif cmd.startswith("set"):
                if self.module is None:
                    print_error("You haven't used any modules yet!")
                    continue
                if len(cmdl) != 3:
                    print_error("Parameter error! Usage: set [parameter name] [parameter value]")
                    continue
                self.set(cmdl[1], cmdl[2])
            elif cmd == "info":
                if self.module is None:
                    print_error("You haven't used any modules yet!")
                    continue
                self.info()
            elif cmd == "back":
                self.module = None
            elif cmd == "":
                continue
            else:
                print_error("There is no such command!")


if __name__ == "__main__":
    ps = PyShell()
    if len(sys.argv) == 1:
        ps.console()
    elif len(sys.argv) == 4:
        try:
            if len(sys.argv[2].split(".")) != 4:
                print_error("Not a valid IP address")
                sys.exit(1)
            elif not (0 < int(sys.argv[3]) <= 65535):
                print_error("Not a valid port number")
                sys.exit(1)
            ps.arg_exploit(sys.argv[1], sys.argv[2], sys.argv[3])
        except TypeError:
            print_error("Not a valid port number")
    elif len(sys.argv) == 2 and sys.argv[1] == "-h":
        print_info("Usage: PyShell [module_name] [host] [port]")
    else:
        print_error("Parameter is incorrect")
        print_info("Usage: PyShell [module_name] [host] [port]")
