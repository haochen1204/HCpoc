import sys
import os
from lib import file

# 版本信息
version = '0.2'

# 当前使用的路径
Pwd = ''

# 判断是否是windows
IS_WIN = IS_WIN = True if (sys.platform in ["win32", "cygwin"] or os.name == "nt") else False

# 输出信息的头部
FIELD_NAMES = {
    'pocs' : ['INDEX','POC PATH','POC NAME'],
    'modules' : ['INDEX', 'MODULE PATH', 'MODULE NAME'],
    'search' : ['INDEX', 'PATH'],
    'module' : ['NAME', 'AUTHOR', 'EXPLAIN'],
    'parameter' : ['PARAMETER','','VALUE'],
    'module result' : ['STATUS','TARGET','MSG'],
    'poc' : ['POC NAME','VUL NAME','VUL NUM','AUTHOR','APP NAME','APP VERSION','EXPLAIN'],
    'poc result' : ['STATUS','TARGET','POC NAME','MSG']
}


# poc的路径和poc的目录信息
POCS,POCS_LIST = file.file().read_pocs()
# 模块的信息
MODULES = file.file().read_modules()
