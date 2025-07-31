# 项目介绍
这是一款用Python开发的漏洞利用脚本，通过此脚本可以获取Shell。每个人都可以提交自己写的exploit，但是需要按照本项目的标准格式写。

# 功能
PyShell可以调用exploit/ 目录下的CVE文件，并执行对应代码来实现漏洞利用。

# 依赖
需要安装colorama库和tabulate库，在命令行使用```pip install colorama```和```pip install tabulate```命令即可

# 使用
直接运行PyShell.py可以进入交互界面，也可以用命令行的方式来快速使用：PyShell.py [模块名称] [目标主机] [端口号]

# 结构描述
```
PyShell.py                // 主程序
tutorial.py               // 示例模块
│
└─exploit                  // 存放exploit模块的目录
    │  CVE-2011-2523.py    // 一个CVE漏洞利用模块
    │  CVE-2012-5106.py
    │  __init__.py
    │
    └─resources            // 其他文件
            base_module.py // CVE漏洞利用模块的基类，所有CVE漏洞都要继承它
            font.py        // 字体库
            shell.py       // 连接shell
            __init__.py
```
# 如何写一个CVE漏洞模块
在exploit/ 目录创建你的漏洞模块，建议文件名改为该漏洞的CVE编号，然后根据tutorial.py的格式写即可

