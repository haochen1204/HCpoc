import os
from lib import config


def read_file(file_dir):
    '''
       读取系统中存在的文件以及目录等信息 
    '''
    # 根据输入的路径对文件内容进行读取并加载到配置文件当中
    for root,dir,files in os.walk(file_dir):
        if  '__pycache__' not in root:
            # 目录文件
            config.PocPwd.append(root)
            # 文件夹
            if '__pycache__' in dir:
                dir.remove('__pycache__')
            config.PocDir[root]=dir
            # 文件
            if '__init__.py' in files:
                files.remove('__init__.py')
            config.PocFile[root]=files

    #print(str(config.PocDir))
    #print(str(config.PocFile))
